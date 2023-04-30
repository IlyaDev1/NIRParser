import sys
import time
import webbrowser
import requests
from bs4 import BeautifulSoup


def getHtml(videoLink, tt):
    time.sleep(5)
    url = 'https://ssstik.io/abc?url=dl'
    form_data = {
        'id': videoLink,
        'locale': 'en',
        'tt': tt
    }
    headers = {
        'Cookie': '__cflb=02DiuEcwseaiqqyPC5qqJA27ysjsZzMZ7vF53ALrfrfyu',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': '*/*'
    }
    server = requests.post(url, data=form_data, headers=headers)
    return server.text

def getLinks(html):
    time.sleep(5)
    soup = BeautifulSoup(html,"html.parser")
    child_soup = soup.find_all('a')
    text = "Without watermark"
    for i in child_soup:
        if (i.string == text):
            return i['href']
