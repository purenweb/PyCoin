import json

from requests import Session
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

#url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {'start': '1', 'limit': '300', 'convert': 'USD'}
headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': '43f1bd77-3f44-46a4-9243-713738fabb72', }
session = Session()
session.headers.update(headers)
response = session.get(url, params=parameters)
data = json.loads(response.text)
def CoinNo(CoinName):
    i=-1
    while True:
        i=i+1
        ss1 = data['data'][i]['name']
        if ss1==CoinName:
            break
    return i


import datetime as dt

mytime = data['status']['timestamp']
mytime = dt.datetime.strptime(mytime[11:19], '%H:%M:%S').time()

mydatetime = dt.datetime.combine(dt.date.today(), mytime) + dt.timedelta(hours=2)
today = mydatetime.strftime("%d/%m/%Y %H:%M:%S")


Dogecoin=data['data'][CoinNo("Dogecoin")]['quote']['USD']['price']
Bitcoin=data['data'][CoinNo("Bitcoin")]['quote']['USD']['price']
XRP=data['data'][CoinNo("XRP")]['quote']['USD']['price']
BitTorrent=data['data'][CoinNo("BitTorrent")]['quote']['USD']['price']
ss=Dogecoin

