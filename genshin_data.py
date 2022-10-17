# https://paimon.moe/items
# 데이터 프레임에 원신 list 수집 업데이트가 되어도 유지가 될 수 있도록 구성

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

url = "https://paimon.moe/items" # url 변수 등록
res = requests.get(url)

soup  = BeautifulSoup(res.text, 'lxml')
MT = soup.select_one('#sapper > main > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(1)') #월요일 목요일
TF = soup.select_one('#sapper > main > div > div:nth-child(4) > div > table > tbody > tr:nth-child(9) > td:nth-child(1)') #화요일 금요일
WS = soup.select_one('#sapper > main > div > div:nth-child(4) > div > table > tbody > tr:nth-child(17) > td:nth-child(1)') #수요일 토요일

days = ['월요일','화요일','수요일','목요일','금요일','토요일']
status = ['캐릭터','무기']
Character = []
weapon = []

# 재료 이름 가져오는 반복문


res = re.compile('<a class=".+">')
# 캐릭터이름을 가져오는 반복문
c_number = [1,2,3,4,9,10,11,12,17,18,19,20]

for i in c_number: #아래로 진행
    check_list = soup.select_one(f'#sapper > main > div > div:nth-child(4) > div > table > tbody > tr:nth-child({i}) > td:nth-child(3)')
    roop = len(res.findall(str(check_list))) #반복문 갯수 확인
    for j in range(1,roop+1):
        Character_name = soup.select_one(f'#sapper > main > div > div:nth-child(4) > div > table > tbody > tr:nth-child({i}) > td:nth-child(3) > a:nth-child({j}) > img')
        Character.append(Character_name['title'])


# 무기 이름 가져오는 반복문
w_number = [5,6,7,8,13,14,15,16,21,22,23,24]

for i in w_number: #아래로 진행
    check_list = soup.select_one(f'#sapper > main > div > div:nth-child(4) > div > table > tbody > tr:nth-child({i}) > td:nth-child(3)')
    roop = len(res.findall(str(check_list))) #반복문 갯수 확인
    for j in range(1,roop+1):
        Character_name = soup.select_one(f'#sapper > main > div > div:nth-child(4) > div > table > tbody > tr:nth-child({i}) > td:nth-child(3) > a:nth-child({j}) > img')
        print(Character_name['title'])

