def declination_of_word(num, words):
    num = abs(num) % 100
    num1 = num % 10
    if num > 10 and num < 20:
        return words[2]
    if num1 > 1 and num < 5:
        return words[1]
    if num1 == 1:
        return words[0]
    return words[2]


print(declination_of_word((8, ['процент', 'процента', 'процентов'])))
