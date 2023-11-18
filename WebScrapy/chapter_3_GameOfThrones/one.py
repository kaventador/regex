import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'
response = requests.get(url)

content = BeautifulSoup(response.text,'html.parser')

episodes = []
# ep_tables = content.find_all('table',class_='wikiepisodetable')
ep_tables = content.select('table.wikiepisodetable')
for table in ep_tables:
    headers = []
    rows = table.find_all('tr')
    for header in table.find('tr').find_all('th'):
        headers.append(header.text)

    for row in table.find_all('tr')[1:]:
            valus = []
            for col in row.find_all(['th','td']):
                valus.append(col.text)

            if valus:
                episode_dic = {headers[i]:valus[i] for i in range(len(valus))}
                episodes.append(episode_dic)

for ep in episodes:
    print(ep)
