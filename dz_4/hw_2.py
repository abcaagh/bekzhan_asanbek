import json
import xml.etree.ElementTree as ET

from requests import get

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
}

response = get(url, headers=headers)
tree = ET.ElementTree(ET.fromstring(response.text)).getroot()
print(tree)