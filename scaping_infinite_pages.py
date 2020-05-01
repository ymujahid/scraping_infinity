import requests
from bs4 import BeautifulSoup
import pprint
from time import time


def check_keyword(page=1):
    url = r'https://lbc.cryptoguru.org/dio/' + str(page)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    tags = soup.find_all('a')
    keyword = '1HjdiADVHew97yM8z4Vqs4iPwMyQHkkuhj'
    # keyword = '1EHNa6Q4Jz2uvNExL497mE43ikXhwF6kZm'
    for i, every_tag in enumerate(tags):
        href = every_tag.get('href', None)
        text = every_tag.getText()
        key = 'https://blockchain.info/address'
        if text == keyword:
            print(f'{keyword} is in index {i} of \'a\' tags list of page {page}')
            return True


t1 = time()
# pp = 904625697166532776746648320380374280100293470930272690489102837043110636675
pp = 100
for p in range(1, pp):
    answer = check_keyword(p)
    if answer:
        print('this is it!')
        break
    print(f'page {p} checked!')
t2 = time()

print(f'it took it {t2 - t1} seconds')
