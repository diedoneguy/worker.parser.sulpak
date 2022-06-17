# from cgitb import html
# from turtle import title
# import requests
# from bs4 import BeautifulSoup
# HOST = 'https://cards.optimabank.kg/'
# URL = 'https://cards.optimabank.kg/premium-cards.html'
# HEADERS = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
# }

# def get_html(url,params=''):
#     r = requests.get(url,headers=HEADERS,params=params)
#     return r 

# def get_content(html):
#     soup = BeautifulSoup(html,'html.parser')
#     items = soup.find_all('div',class_="row-fluid card-info")
#     cards = []

#     for item in items:
#         cards.append({
#                 'title':item.find('div',class_="offset1 span8").find('a').get('href'),
#                 'card_image':item.find('div',class_="card-img").find('img').get('src')
#         })

#     file = open('card.csv','a')
#     file.write(str(f'Имя карты:{title}'))
#     return cards


# html = get_html(URL)
# print(get_content(html.text))
from turtle import title
import requests
from bs4 import BeautifulSoup
HOST = 'https://www.sulpak.kg/'
URL = 'https://www.sulpak.kg/f/noutbuki'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
def get_html(url,params=''):
    r = requests.get(url,headers=HEADERS,params=params,verify=False)#отправляем запрос на сайт и на параметры и на хидерс это обязательно
    return r 

def get_content(html):
    soup = BeautifulSoup(html,'html.parser') #созд переменную и принимаем html и через html.parser и получаем html
    items = soup.find_all('div',class_="goods-tiles")#ищем все из дивки good-tiles
    cards = []

    for item in items:
        cards.append({
                # 'title':item.find('div',class_="product-container-right-side").get_text(),
            'title':item.find('div',class_="product-container-right-side").find('h3').get_text(strip=True),
            'price':item.find('div',class_="price").get_text(strip=True)
                
        })
    return cards


html = get_html(URL)
file = open('sulpak.csv','a')
file.write(str(f'{get_content(html.text)}\n\n'))
print(get_content(html.text))



