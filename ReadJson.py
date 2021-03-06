import json
from requests import Session
def ReadJson():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {'start': '1', 'limit': '300', 'convert': 'USD'}
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': '43f1bd77-3f44-46a4-9243-713738fabb72', }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    def CoinNo(codename):
        i = -1
        while True:
            i = i + 1
            sCoinName = data['data'][i]['name']
            if sCoinName == codename:
                break
        return i

    import datetime as dt
    time = dt.datetime.strptime(data['status']['timestamp'][11:19], '%H:%M:%S').time()
    datetime = dt.datetime.combine(dt.date.today(), time) + dt.timedelta(hours=2)
    sToday = datetime.strftime("%d/%m/%Y %H:%M:%S")
    time = datetime.strftime("%H:%M:%S")


    Dogecoin = data['data'][CoinNo("Dogecoin")]['quote']['USD']['price']
    Bitcoin = data['data'][CoinNo("Bitcoin")]['quote']['USD']['price']
    XRP = data['data'][CoinNo("XRP")]['quote']['USD']['price']
    BitTorrent = data['data'][CoinNo("BitTorrent")]['quote']['USD']['price']
    retVal = str(Dogecoin) + "," + str(Bitcoin) + "," + str(XRP) + "," + str(BitTorrent) + "," + str(time) + "," + str(sToday)
    return retVal
