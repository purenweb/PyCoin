import json

from requests import Session
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

#url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {'start': '1', 'limit': '100', 'convert': 'USD'}
headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': '43f1bd77-3f44-46a4-9243-713738fabb72', }

session = Session()
session.headers.update(headers)


response = session.get(url, params=parameters)
data = json.loads(response.text)


ss=data['data'][9]['quote']['USD']['price']

def deep_search(needles, haystack):
    found = {}
    if type(needles) != type([]):
        needles = [needles]

    if type(haystack) == type(dict()):
        for needle in needles:
            if needle in haystack.keys():
                found[needle] = haystack[needle]
            elif len(haystack.keys()) > 0:
                for key in haystack.keys():
                    result = deep_search(needle, haystack[key])
                    if result:
                        for k, v in result.items():
                            found[k] = v
    elif type(haystack) == type([]):
        for node in haystack:
            result = deep_search(needles, node)
            if result:
                for k, v in result.items():
                    found[k] = v
    return found


xxx = deep_search(["Dogecoin", "Dogecoin"], json.loads(response.text))
