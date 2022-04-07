def odd_nums_gen(max_num):
    for num in range(1, max_num + 1):
        if num % 2 != 0:
            yield num
odd_num = odd_nums_gen(15)
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
