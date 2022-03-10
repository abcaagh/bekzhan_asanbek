from requests import get

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
a = response.content
print(a)


def currency_rates(val):
    return