import requests
import re
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'
articles = []
r = requests.get(url)
content = BeautifulSoup(r.text,'html.parser')

for item in content.find_all('tr',class_='athing'):
    item_a = item.find('a',class_='itemlink')
    item_link = item_a.get("href") if item_a else None
    item_text = item_a.get_text(strip=True) if item_a else None
    next_row = item.find_next_sibling('tr')
    item_score = next_row.find('span',class_='score')
