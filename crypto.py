import requests
from bs4 import BeautifulSoup


coin_market_cup = 'https://coinmarketcap.com/'

headedrs = {
    'User-Agent:' 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

resp = requests.get(url, headedrs=headedrs).text
soup = BeautifulSoup(resp, 'lxml')

tbody = soup.find('tbody')
coins = soup.find_all('tr')

for coin in coins:
    name = coin.find(class_="cmc-link").get("href").replace("/currencies/", "")[:-1]
    price = coin.find(class_="sc-131di3y-0 cLg00r")

    if price:
        f'{name}:{price.text}'
    else:
        price = coin.find_all("td")[-2].find("span").text
        f'{name}:{price}'