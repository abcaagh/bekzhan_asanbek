odd_nums_cube = []
i = 1
while i < 1000:
    if i % 2 != 0:
        odd_nums_cube.append(i ** 3)
    i += 1


def amount_of_digits(num):
    place_value = 1
    i = 1
    while i <= 11:
        if 0 < num // place_value <= 9:
            return i
        i += 1
        place_value *= 10


def summ_digits():
    i = 0
    while i < len(odd_nums_cube):
        result = odd_nums_cube[i] // 1000 + odd_nums_cube[i] // 100 % 10 + odd_nums_cube[i] % 100 // 10 + odd_nums_cube[
            i] % 10
        if result // 7 == 0:
            odd_nums_cube[i] = result
            break
        i += 1


def add_seven(nums):
    i = 0
    for i in range(len(nums)):
        nums[i] += 7


summ_digits()
add_seven(odd_nums_cube)
