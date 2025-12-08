from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import json  

# 1. WSGI FIX: We must ensure the Flask app is named 'application' in the WSGI file,
# but using 'app' here is fine as long as the WSGI file imports it correctly.
app = Flask(__name__)
CORS(app)

# We define a 'User-Agent' so Wikipedia thinks we are a browser, not a bot.
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def get_soup(url):
  r = requests.get(url, headers=headers)
  r.raise_for_status()
  html = r.text.encode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  return soup

def get_categories(url):
  soup = get_soup(url)
  data = {}
  categories = soup.find_all("dl")
  for category in categories:
    category_name = category.find("dt").get_text().strip()
    category_animals = category.find_all("a")
    data[category_name] = [
      {"name": animal.get_text().strip(), "url": animal.get("href")
      } 
      for animal in category_animals if animal.get("href")
    ]
  return data

WIKIPEDIA_BASE_URL = "https://en.wikipedia.org"

def get_animal_class(relative_url):
  try:
    full_url = WIKIPEDIA_BASE_URL + relative_url
    soup = get_soup(full_url)
    table = soup.find("table", {"class": "infobox biota"})
    if not table:
      return "Unknown"
    rows = table.find_all("tr")
    for row in rows:
      # Check both 'Class' and 'Classis' (Latin) for robustness
      if "Class:" in row.get_text() or "Classis:" in row.get_text():
        # Find the first link within the data cell, assuming the class name is a link
        link = row.find('td').find('a')
        if link:
            return link.get_text().strip()
    return "Unknown"
  except Exception as e:
    # Log the error for debugging purposes
    print(f"Error fetching animal class for URL {full_url}: {e}")
    return "Error"

# 2. FIX: ADD A ROOT ROUTE TO RESOLVE THE 404 ERROR
@app.route('/', methods=['GET'])
def index():
    """A simple root route to confirm the application is running."""
    return jsonify({
        "status": "ok",
        "message": "Welcome to the Endangered Species API!",
        "endpoints": {
            "scrape": "/api/scrape",
            "data": "/api/data"
        }
    })

@app.route('/api/scrape', methods=['GET'])
def scrape_data():
  """Scrape all data and return it"""
  # NOTE: The scraping will hit external websites which may be slow or blocked.
  # If you see 502/504 errors again, it may be due to a timeout.
  category_data = get_categories(
    "https://skillcrush.github.io/web-scraping-endangered-species/"
  )
  
  # Ensure the JSON file can be written now that you have paid for more space.
  for category in category_data:
    for animal in category_data[category]:
      animal['class'] = get_animal_class(animal['url'])
  
  with open('endangered_species.json', 'w') as f:
    json.dump(category_data, f, indent=2)
  
  return jsonify(category_data)

@app.route('/api/data', methods=['GET'])
def get_data():
  """Return cached data if available"""
  try:
    with open('endangered_species.json', 'r') as f:
      data = json.load(f)
    return jsonify(data)
  except FileNotFoundError:
    return jsonify({"error": "No data available. Call /api/scrape first"}), 404

# 3. FIX: REMOVE THE app.run() CALL! PythonAnywhere handles the server process.
# if __name__ == '__main__':
#   app.run(debug=True, port=5000)