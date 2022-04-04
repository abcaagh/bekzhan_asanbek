from requests import get

url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
resp = get(url).text

log = resp.split('\n')
list_log = []

for el in log:
    el_info = el.split(' ')
    if len(el_info) > 1:
        list_log.append((el_info[0], el_info[5][1:], el_info[6]))

print(*list_log, sep='\n')
