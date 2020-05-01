import requests
from bs4 import BeautifulSoup
import pprint
from time import time


def my_decorator():
    pass


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
# for p in range(944, 10000):
#     answer = check_keyword(p)
#     if answer:
#         print('this is it!')
#     print(f'page {p} checked!')
p = 65432178905682168979216398732907210382036897238023
print(check_keyword(p))
print(f'page {p} checked!')
t2 = time()

print(f'it took it {t2 - t1} seconds')
