import os                                #СОЗДАНИЕ ПАПОК
path = 'C:\\Users\\TUFman\\Desktop\\python\\python\\'
projectname = 'dataset'
folders = ['tigers', 'leopardes']

def createfolder(path):
    if not os.path.exists(path):
        os.mkdir(path)

fullpath = os.path.join(path, projectname)
createfolder(fullpath)

for f in folders:
    folder = os.path.join(fullpath, f)
    createfolder(folder)

!pip install beautifulsoup4

import time

import requests
from bs4 import BeautifulSoup



url = "https://yandex.ru/images/search?text=tiger&from=tabbar"

r = requests.get(url)
r.text

soup = BeautifulSoup(r.text, 'lxml')
soup

blocks = soup.findAll('div', class_='serp-item__preview')
count = 0

for block in blocks:
    if (block):
        preview_block = block.find('a', class_='serp-item__link').get('href')
        link = (preview_block.split('=')[3])
        link2 = link.replace('%3A', ':')
        link3 = link2.replace('%2F', '/')
        link4 = (link3.split('&')[0])
        print(link4)
        try:
            image_byt = requests.get(f'{link4}').content
            time.sleep(1)
            with open(f'C:\\Users\\TUFman\\Desktop\\python\\python\\dataset\\tigers\\{count}.jpg', 'wb') as file:
                file.write(image_byt)
            count += 1
            print(count)
        except:
            continue