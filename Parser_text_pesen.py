import requests
from bs4 import BeautifulSoup
import fake_useragent
import json
prodeject_list = []
num = 0

user = fake_useragent.UserAgent().random
header = {'user-agent':user}
for i in range(1919):
    url = (f'https://www.beesona.ru/songs/p{i}/')
    res = requests.get(url, headers=header)
    soup = BeautifulSoup(res.text, 'lxml')
    item = soup.find('div', class_='row xls')
    items = item.find_all('div',class_='col-md-6')
    num += 1
    print(f'{num} страница из 1919')
    for osnova in items:
        sulka = 'https://www.beesona.ru' + osnova.find('a').get('href')
        res = requests.get(sulka, headers=header)
        soup = BeautifulSoup(res.text, 'lxml')
        item = soup.find('div', class_='copys')
        nazvanie_pesni = item.find('b', class_='m153').text
        text_pesni = item.find('div', class_='m207').text
        prodeject_list.append(
         {
                'Название песни': nazvanie_pesni,
               'Текст песни' : text_pesni,
            }
        )

    with open('text_pesen.json', 'a', encoding="utf-8") as file:
        json.dump(prodeject_list, file, indent=4, ensure_ascii=False)