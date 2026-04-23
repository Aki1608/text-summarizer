import requests
from bs4 import BeautifulSoup

def extract_txt_from_url(URL):
    # This will 
    text = ""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    r = requests.get(URL, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    all_paragraphs = soup.find_all('p')
    for paragraph in all_paragraphs:
        text += paragraph.text + "  "
    
    return text
