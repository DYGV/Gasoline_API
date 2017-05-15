# coding: utf-8
import requests
import json


def main():
    url = 'http://127.0.0.1:8000/api/gasoline/'

    # お好みで
    payload = {
        'rank': '',
        'pref': '',
        'price': '',
        'date': '',
    }

    response = requests.get(url, params=payload)
    res_json = json.loads(response.text)
    for ranking in res_json:
        rank = ranking['rank']
        pref = ranking['pref']
        price = ranking['price']
        print("順位:{rank} {pref} {price}".format(rank=rank, pref=pref, price=price))

if __name__ == '__main__':
    main()
