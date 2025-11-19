import requests
from bs4 import BeautifulSoup

# We define a 'User-Agent' so Wikipedia thinks we are a browser, not a bot.
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# We add 'headers=headers' to the request
honey_badger = requests.get("https://en.wikipedia.org/wiki/Honey_badger", headers=headers)
# --- END OF FIX ---

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
    data[category_name] = category_animals
  return data

def get_animal(url):
  soup = get_soup(url)
  table = soup.find("table", {"class": "infobox biota"})
  if not table:
    return "No class found."
  rows = table.find_all("tr")
  for row in rows:
    if "Class:" in row.get_text():
      animal_class = row.find("a").contents[0]
      return animal_class

category_data = get_categories("https://skillcrush.github.io/web-scraping-endangered-species/")

animal_class = get_animal("https://en.wikipedia.org/wiki/Honey_badger")

print(animal_class)
