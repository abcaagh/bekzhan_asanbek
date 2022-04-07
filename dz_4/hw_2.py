from requests import get

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
resp = get(url)
src = resp.text
valuta_list = []

for _ in range(len(src)):
    start_index = src.find('<Valute ID')
    last_index = src.find('</Valute>') + 9
    if start_index == -1:
        break
    valuta_list.append(src[start_index:last_index])
    src = src[last_index:]


def currency_rates(val):
    for el in valuta_list:
        if el.find(val.upper()) != -1:
            value = el[el.find('Value') + 6:el.rfind('Value') - 2]
            return float(value.replace(',', '.'))
    return None

print(f'1 рубль равен {currency_rates("USD")} доллару')
print(f"1 рубль равен {currency_rates('EUR')} евро")
