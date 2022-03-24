from copy import copy
from random import uniform

price = []
price_desc = []
for i in range(15):
    rnd = round(uniform(1.0, 100.0), 2)
    price.append(rnd)
for i in range(len(price)):
    float_num = int(round(price[i] % int(price[i]), 2) * 100)
    print(f'{int(price[i])} рубль {float_num} копеек', end=',')
else:
    print()
    print(id(price), 'id before sorting')
    price.sort()
    print(id(price), 'id after sorting')
    price_desc = copy(price)
    price_desc.sort(reverse=True)
    print(id(price_desc), 'id desc sorted', price_desc)

print(price)
i = 0
j = 1
while i < len(price)-1:
    while j < len(price):
        if price[j] > price[i]:
            temp = price[i]
            price[i] = price[j]
            price[j] = temp
        j = i + 1
    i += 1
print(price, 'd')
# for i in range(len(price)):
#     for j in range(len(price)):
#         if price[j+1] > price[i]:
#             temp = price[i]
#             price[i] = price[j]
#             price[j] = temp
