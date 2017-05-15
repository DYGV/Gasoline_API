# coding: utf-8
from urllib import request
from bs4 import BeautifulSoup
import os
import django


def update():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
    django.setup()
    from APIs.models import Gasoline, HighOctane, Diesel
    response = request.urlopen('https://e-nenpi.com/gs/prefavg')
    body = response.read()
    soup = BeautifulSoup(body, 'html.parser')
    tr_tag = soup.find_all('tr')  # trタグ取得

    # Gasoline.objects.all().delete()
    # HighOctane.objects.all().delete()
    # Diesel.objects.all().delete()

    for ranking in tr_tag:
        try:
            rank = ranking.td.string  # 順位
            pref = ranking.find_all('td', {'class': 'pref'})    # 都道府県名
            price = ranking.find_all('td', {'class': 'price'})  # 価格

            # レギュラー
            gasoline_pref = pref[0].string
            gasoline_price = price[0].string
            # ハイオク
            highoctane_pref = pref[1].string
            highoctane_price = price[1].string
            # 軽油
            diesel_pref = pref[2].string
            diesel_price = price[2].string

            Gasoline.objects.create(rank=rank, pref=gasoline_pref, price=gasoline_price)
            HighOctane.objects.create(rank=rank, pref=highoctane_pref, price=highoctane_price)
            Diesel.objects.create(rank=rank, pref=diesel_pref, price=diesel_price)

        except:
            pass    # クローリング先の"tr"タグに関係ない内容が含まれている分


if __name__ == '__main__':
    update()

