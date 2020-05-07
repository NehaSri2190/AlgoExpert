#!/usr/bin/env python3
import xlsxwriter
import datetime
import requests

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'df62caf4-0f9b-45ba-8504-0b24ab672ef0',
}

session = Session()
session.headers.update(headers)

sno = ['sno']
name = ['Name']
symbol = ['Symbol']
max_supply = ['Max Supply']
circ_supply = ['Circulation Supply']
total_supply = ['Total Supply']
price =['Price']
volume = ['Volume']
perc1h = ['% 1 hour']
perc24h = ['% 24 hours']
perc7d = ['% 7 days']
market = ['Market Supply']
ts = ['Last Updated']

x = datetime.datetime.now()
d = (x.strftime("%d") )
m = (x.strftime("%m"))
y = (x.strftime("%y"))

try:
  response = session.get(url, params=parameters)
  data = response.text
  data = str(data)
  data.encode(encoding='UTF-8', errors='strict')
  f = open("coinmarketcap.txt", 'w')
  f.write(data)
  f.close()

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

OutFile = ('CoinMarketCap' + d + '-' + m + '-'+ y + '.xlsx')

f = open("coinmarketcap.txt", "r")

headers = [sno, name, symbol,max_supply,circ_supply,total_supply,price,volume,perc7d,perc1h,perc24h,market,ts]

workbook = xlsxwriter.Workbook(OutFile)
worksheet = workbook.add_worksheet()

for x in f:
    if '            "id":' in x and '                "id":' not in x:

        temp = x.replace('"id":','')
        temp = temp.strip()
        temp = temp.strip(',')
        sno.append(temp)

    if '"name":' in x and '                "name": ' not in x:

        temp = x.replace('"name":','')
        temp = temp.strip()
        temp = temp.strip(',')
        name.append(temp)

    if 'symbol":' in x and '                "symbol":' not in x:

        temp = x.replace('"symbol":','')
        temp = temp.strip()
        temp = temp.strip(',')
        symbol.append(temp)

    if '"max_supply":' in x:
        temp = x.replace('"max_supply":','')
        temp = temp.strip()
        temp = temp.strip(',')
        max_supply.append(temp)
    if '"circulating_supply":' in x:
        temp = x.replace('"circulating_supply":','')
        temp = temp.strip()
        temp = temp.strip(',')
        circ_supply.append(temp)
    if '"total_supply":' in x:
        temp = x.replace('"total_supply":','')
        temp = temp.strip()
        temp = temp.strip(',')
        total_supply.append(temp)

    if '"price":' in x:
        temp = x.replace('"price":','')
        temp = temp.strip()
        temp = temp.strip(',')
        price.append(temp)

    if '"volume_24h":' in x :
        temp = x.replace('"volume_24h":','')
        temp = temp.strip()
        temp = temp.strip(',')
        volume.append(temp)

    if '"percent_change_1h":' in x :
        temp = x.replace('"percent_change_1h":','')
        temp = temp.strip()
        temp = temp.strip(',')
        perc1h.append(temp)

    if '"percent_change_24h":' in x :
        temp = x.replace('"percent_change_24h":','')
        temp = temp.strip()
        temp = temp.strip(',')
        perc24h.append(temp)

    if '"percent_change_7d":' in x :
        temp = x.replace('"percent_change_7d":','')
        temp = temp.strip()
        temp = temp.strip(',')
        perc7d.append(temp)

    if '"market_cap":' in x :
        temp = x.replace('"market_cap":','')
        temp = temp.strip()
        temp = temp.strip(',')
        market.append(temp)

    if '            "last_updated":' in x and '                    "last_updated":' not in x:

        temp = x.replace('"last_updated":','')
        temp = temp.strip()
        temp = temp.strip(',')
        ts.append(temp)
col = 0
row = 0
while col < len(headers):

    for items in headers:
        while (row < len(items)):
            for values in items:
                worksheet.write(row, col, values)
                row = row + 1
        col = col + 1
        row = 0

workbook.close()
f.close()