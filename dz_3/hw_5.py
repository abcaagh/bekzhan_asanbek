import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

joke_element = [nouns, adverbs, adjectives]

def rand_num():
    i = random.randint(0, len(nouns[:-1]))
    return i

def get_jokes(sum):
    joke = ''
    joke_list = []
    j = 0
    for i in range(len(joke_element)):
        joke.join(joke_element[i][rand_num()])
    print(joke)


get_jokes(2)
