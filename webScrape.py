import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

url = "https://www.imdb.com/chart/top"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

sleep(1)
elements = soup.select('li.ipc-metadata-list-summary-item.sc-10233bc-0.iherUv.cli-parent h3.ipc-title__text')

top_movies = []

sleep(1)
print("Gathering data...")
for title in elements:
    print(title.text)