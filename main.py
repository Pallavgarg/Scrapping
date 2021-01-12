import requests
from bs4 import BeautifulSoup
import html5lib
import os
import json

usr_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

SAVE_FOLDER = 'image_folder'

def main():
    if not os.path.exists(SAVE_FOLDER):
        os.makedir(SAVE_FOLDER)
    download_images()


def download_images():
    data = input('What are you looking for ? ')
    n_images = int(input("How many image do you want ? "))
    print("Start searching...")

    searchurl = 'https://www.google.com/search?hl=jp&q=' + data + '&btnG=Google+Search&tbs=0&safe=off&tbm=isch'
    #print(searchurl)

    response = requests.get(searchurl,headers=usr_agent)
    html = response.text

    # find all divs where class='rg_meta'
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find_all('img')
    all_link = set()
    for link in result:
        if(link.get('data-src')!=None):
            linkText = link.get('data-src')
            all_link.add(linkText)

    print("Start Downloading...")

    count=0

    for imagelink in all_link:
        if count<=n_images:
            response = requests.get(imagelink)

            imagename = SAVE_FOLDER + '/' + data + str(count) + '.jpg'
            print(imagename + " downloaded")
            with open(imagename, 'wb') as file:
                file.write(response.content)
        count+=1









if __name__ == '__main__':
    main()