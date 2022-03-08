num_translations = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(num):
    translation = ''
    for en, ru in num_translations.items():
        if (en == num):
            return num_translations.get(num)
        elif (ru == num):
            return en
        else:
            translation = 'None'
    return translation


print(num_translate('two'))
