import requests
from bs4 import BeautifulSoup

# We define a 'User-Agent' so Wikipedia thinks we are a browser, not a bot.
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# We add 'headers=headers' to the request
honey_badger = requests.get("https://en.wikipedia.org/wiki/Honey_badger", headers=headers)
# --- END OF FIX ---
honey_badger.raise_for_status()
honey_badger_html = honey_badger.text.encode("utf-8")
honey_badger_soup = BeautifulSoup(honey_badger_html, 'html.parser')

h2 = honey_badger_soup.find_all("h2")

print(len(h2))

for element in h2:
  print(element)

links = honey_badger_soup.find_all("a")
print(links[:5])

images = honey_badger_soup.find_all("img")
print(images[:-4])