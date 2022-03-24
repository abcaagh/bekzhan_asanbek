from bs4 import BeautifulSoup
from requests import get


def currency_rates(val):
    response = get('http://cbr.ru/scripts/XML_daily.asp')
    src = response.text
    soup = BeautifulSoup(src, "lxml")
    currency = []

    num_code = soup.find_all("numcode")
    char_code = soup.find_all("charcode")
    name = soup.find_all("name")
    value = soup.find_all("value")

    i = 0
    while i < len(name):
        currency.append({
            "name": name[i].text,
            "char_code": char_code[i].text,
            "value": value[i].text,
            "num_code": num_code[i].text,
        })
        i += 1
    for item in range(len(currency)):
        if currency[item]['char_code'] == val:
            return currency[item]['value']
        else:
            print("None")


print(f'{currency_rates("AUD")}')
