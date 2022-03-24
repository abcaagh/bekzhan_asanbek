en_nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
ru_nums = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']


def num_translations(num_to_translate):
    is_title = num_to_translate.istitle()
    translation = None
    for en, ru in zip(en_nums, ru_nums):
        if num_to_translate.lower() == en:
            if is_title:
                translation = ru.title()
            else:
                translation = ru
        elif num_to_translate.lower() == ru:
            if is_title:
                translation = en.title()
            else:
                translation = en
    print(translation)


num_translations('Two')
