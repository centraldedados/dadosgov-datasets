#!/usr/bin/env python3
from secrets import apikey
import requests
import pandas as pd

session = requests.Session()
session.headers.update({'X-API-KEY': apikey})
response = session.get('https://dados.gov.pt/api/1/datasets/')

datasets = response.json().get('data')
next_page = response.json().get('next_page')
while next_page:
    response = session.get(next_page)
    datasets += response.json().get('data')
    next_page = response.json().get('next_page')
    print(next_page)
    if not next_page:
        print('Tá feito!')
        break

df = pd.DataFrame(datasets)
outfile = open('../data/datasets.json', 'w')
outfile.write(df.to_json(orient='records', force_ascii=False, lines=True))
