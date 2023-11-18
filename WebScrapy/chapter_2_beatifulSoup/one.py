import requests
from bs4 import BeautifulSoup
import re

url = 'https://en.wikipedia.org/wiki/Mao_Zedong'

response = requests.get(url)
content = BeautifulSoup(response.text,'html.parser')

# print(content.find_all(['h1','h2']))
# print(content.find('h1').attrs)
# print(content.find('h1').text)
# print(content.find(attrs={'role':'main'}))
#
# print(content.find(class_='mw-indicator'))
# print(content.find('a','mw-indicator'))

# print(content.find_all('h2',limit=5))
# print(content.find('h2').get('id'))

# print(content.find(re.compile('^d')))

# print(content.select('li > a[title="Benjamin Tucker"]'))

