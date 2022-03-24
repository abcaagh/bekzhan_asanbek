from builtins import enumerate

weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
           'была', '+5', 'градусов']
quotes_ind = []

for i, j in enumerate(weather):
    if weather[i].isdigit():
        weather[i] = f'{int(weather[i]):.2f}'
        quotes_ind.append(i)
        continue
    for j, char in enumerate(weather[i]):
        if char.isdigit():
            weather[i] = f'+{int(weather[i][j]):.2f}'
            quotes_ind.append(i)

quotes_ind.reverse()

for i in quotes_ind:
    weather.insert(i, '"')
    weather.insert(i + 2, '"')
print(weather)

weather_str = ' '.join(weather)
print(weather_str)

