#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests
from pyquery import PyQuery as pq


url = 'https://kjh.55128.cn/sd-history-2022.htm'

res = requests.get(url)
doc = pq(res.text)


trs = doc('tbody tr')

data = []
for tr in trs:
    no = pq(tr).find('td:nth-child(2)').text()
    value = pq(tr).find('td:nth-child(3)').text().replace(" ", "")
    data.append(f"{no} {value}")

with open('kaipiao.txt', 'w', encoding='utf8') as f:
    for v in data:
        f.write(v+"\n")

print('finish')