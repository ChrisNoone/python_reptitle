# coding: utf-8

import requests
from urllib import error
from bs4 import BeautifulSoup

url = 'https://github.com/login/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
}
rsp = requests.get(url, headers=headers)
cookies = rsp.cookies.get_dict()
html = BeautifulSoup(rsp.text, 'lxml')
token = html.find(name='input', attrs={'name': 'authenticity_token'}).get('value')
url2 = 'https://github.com/session/'
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
}
data = {
    'login': '@email',
    'password': '@password',
    'authenticity_token': token
}
rsp2 = requests.post(url2, params=data, headers=headers2, cookies=cookies)
html2 = BeautifulSoup(rsp2.text, 'lxml')
cookies = rsp2.cookies.get_dict()
url3 = 'https://github.com/ChrisNoone?tab=repositories'
headers3 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
}
rsp3 = requests.get(url3, headers=headers3, cookies=cookies)
html3 = BeautifulSoup(rsp3.text, 'lxml')
print(html3)
