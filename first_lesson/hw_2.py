cub = []
i = 0
sum = 0
while i < 1000:
    if not i % 2 == 0:
        cub.append(str(i ** 3))
    i += 1
for i in range(len(cub)):
    print(len(cub[i]))
    for j in range(len(cub[i])):
        sum = sum + int(cub[i][j])
    if not sum % 7 == 0:
        cub.remove(cub[i])
    sum = 0
