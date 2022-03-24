def declination_of_word(num, words):
    num = abs(num) % 100
    num1 = num % 10
    if num1 == 1:
        return words[0]
    elif num1 > 1 and num < 5:
        return words[1]
    return words[2]


i = 0
while i < 100:
    i += 1
    print(i, ' ', declination_of_word(i, ['процент', 'процента', 'процентов']))
