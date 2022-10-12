# https://paimon.moe/items
# 데이터 프레임에 원신 list 수집

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://paimon.moe/items" # url 변수 등록
res = requests.get(url)

soup  = BeautifulSoup(res.text, 'lxml')
test = soup.select_one('#sapper > main > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(1)') 
test = soup.select_one('#sapper > main > div > div:nth-child(4) > div > table > tbody > tr:nth-child(9) > td:nth-child(1)')
test = soup.select_one('#sapper > main > div > div:nth-child(4) > div > table > tbody > tr:nth-child(17) > td:nth-child(1)')
print(test.text)


