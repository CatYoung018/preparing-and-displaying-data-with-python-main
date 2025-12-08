# main.py

from flask import Flask, jsonify, send_from_directory, current_app 
from flask_cors import CORS
import requests
import os
from bs4 import BeautifulSoup
import json  

# --- FLASK APP SETUP ---

# We must ensure the Flask app is named 'application' in the WSGI file.
app = Flask(__name__)
CORS(app)

# We define a 'User-Agent' so Wikipedia thinks we are a browser, not a bot.
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

WIKIPEDIA_BASE_URL = "https://en.wikipedia.org"


# --- UTILITY FUNCTIONS ---

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

def get_animal_class(relative_url):
  try:
    full_url = WIKIPEDIA_BASE_URL + relative_url
    soup = get_soup(full_url)
    table = soup.find("table", {"class": "infobox biota"})
    if not table:
      return "Unknown"
    rows = table.find_all("tr")
    for row in rows:
      if "Class:" in row.get_text() or "Classis:" in row.get_text():
        link = row.find('td').find('a')
        if link:
            return link.get_text().strip()
    return "Unknown"
  except Exception as e:
    print(f"Error fetching animal class for URL {full_url}: {e}")
    return "Error"


# --- FLASK ROUTES ---

# 1. SERVE STATIC FILES (FIX for PythonAnywhere loading errors)
@app.route('/')
def index():
    """Serves the main HTML file from the application root."""
    # Use current_app.root_path for robust file location
    return send_from_directory(current_app.root_path, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serves all other static files (CSS, JS, images) from the application root."""
    return send_from_directory(current_app.root_path, filename)


# 2. CACHED DATA ENDPOINT (FAST LOAD)
@app.route('/api/data', methods=['GET'])
def get_data():
  """Return cached data if available, using robust file path."""
  try:
    # Use absolute path to ensure the file is found
    file_path = os.path.join(current_app.root_path, 'endangered_species.json')
    with open(file_path, 'r', encoding='utf-8') as f:
      data = json.load(f)
    return jsonify(data)
  except FileNotFoundError:
    return jsonify({"error": "No data available. Please scrape first."}), 404

# 3. SCRAPING ENDPOINT (SLOW/Development only)
@app.route('/api/scrape', methods=['GET'])
def scrape_data():
  """Scrape all data and return it, then save it to the JSON file."""
  category_data = get_categories(
    "https://skillcrush.github.io/web-scraping-endangered-species/"
  )
  
  # Fetch animal classes
  for category in category_data:
    for animal in category_data[category]:
      animal['class'] = get_animal_class(animal['url'])
  
  # Save to file
  file_path = os.path.join(current_app.root_path, 'endangered_species.json')
  with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(category_data, f, indent=2)
  
  return jsonify(category_data)


# 4. REMOVE app.run() for PythonAnywhere deployment
# if __name__ == '__main__':
#   app.run(debug=True, port=5000)