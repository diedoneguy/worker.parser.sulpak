from cgitb import html
from turtle import title
import requests
from bs4 import BeautifulSoup
HOST = 'https://cards.optimabank.kg/'
URL = 'https://cards.optimabank.kg/premium-cards.html'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

def get_html(url,params=''):
    r = requests.get(url,headers=HEADERS,params=params)
    return r 

def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div',class_="row-fluid card-info")
    cards = []

    for item in items:
        cards.append({
                'title':item.find('div',class_="offset1 span8").find('a').get('href'),
                'card_image':item.find('div',class_="card-img").find('img').get('src')
        })

    file = open('card.csv','a')
    file.write(str(f'Имя карты:{title}'))
    return cards


html = get_html(URL)
print(get_content(html.text))




