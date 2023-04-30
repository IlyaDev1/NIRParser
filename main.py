import requests
from bs4 import BeautifulSoup as bs
import key
import time
import script
from extract_frames import geno

def users():
    user = []
    file = open('Users.txt')
    for line in file:
        user.append('https://www.tiktok.com/@'+line[:len(line)-1])
    file.close()
    return user


def OnlyLink(s):
    s = str(s)
    index = [0, 0]
    for i in range(len(s)):
        if s[i] == '"' and index[0] == 0:
            index[0] = i
        elif s[i] == '"' and index[0] != 0:
            index[1] = i
            break
    return s[index[0]+1:index[1]]


def getVideoLinks(link):
    Links = []
    OldLink = link
    link = requests.get(link)
    html = bs(link.content, 'html.parser')
    s = f'[href^="{OldLink}/video"]'
    for el in html.select(f'{s}'):
        Links.append(OnlyLink(el))
    return Links


def download():
    count = 0
    links = users()
    mas = []
    for i in range(len(links)):
        mas.append(getVideoLinks(links[i]))

    for i in range(len(mas) - 7):
        for j in range(len(mas[i])):
            time.sleep(3)
            VideoLink = str(mas[i][j])
            tt = 'dEs4cnY3'
            downloadLink = key.getLinks(key.getHtml(VideoLink,tt))
            print(downloadLink)
            key.webbrowser.open(downloadLink)
            count += 1

        time.sleep(3)
        script.ReName(i, len(mas[i]))


download()
time.sleep(5)
geno()
