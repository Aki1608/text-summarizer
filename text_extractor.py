import requests
from bs4 import BeautifulSoup

text = ""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
Article_URL = 'https://en.wikipedia.org/wiki/SpaceX'

r = requests.get(Article_URL, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
all_paragraphs = soup.find_all('p')
for paragraph in all_paragraphs:
    text += paragraph.text + "  "

print(text[:1000])