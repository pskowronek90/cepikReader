import urllib.request
import json
from collections import Counter

import io

url = "https://api.cepik.gov.pl//pojazdy?wojewodztwo=30&data-od=20190101&data-do=20191231"

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

allBrands = []
categorizedBrands = []

for i in data['data']:
    allBrands.append(i['attributes']['marka']) 

result = dict(Counter(allBrands))

for key, value in result.items():
    categorizedBrands.append({"brand": key, "amount": value})

categorizedBrands.sort(key = lambda x:x["amount"], reverse=True)

with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(categorizedBrands, outfile, sort_keys = True, ensure_ascii=False, indent=4)

