from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import json  # YOU NEED THIS!

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
    category_name = category.find("dt").get_text()
    category_animals = category.find_all("a")
    data[category_name] = [
      {"name": animal.get_text(), "url": animal["href"]} 
      for animal in category_animals
    ]
  return data

def get_animal_class(url):
  try:
    soup = get_soup(url)
    table = soup.find("table", {"class": "infobox biota"})
    if not table:
      return "Unknown"
    rows = table.find_all("tr")
    for row in rows:
      if "Class:" in row.get_text():
        animal_class = row.find("a").contents[0]
        return animal_class
    return "Unknown"
  except Exception as e:
    return "Error"

@app.route('/api/scrape', methods=['GET'])
def scrape_data():
  """Scrape all data and return it"""
  category_data = get_categories(
    "https://skillcrush.github.io/web-scraping-endangered-species/"
  )
  
  # THESE LINES MUST BE INDENTED - they're inside the function!
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

if __name__ == '__main__':
  app.run(debug=True, port=5000)