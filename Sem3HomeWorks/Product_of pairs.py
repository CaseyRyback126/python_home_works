# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  Пример:  - [2, 3, 4, 5, 6] => [12, 15, 16];
#           - [2, 3, 5, 6] => [12, 15]

from random import randint


def get_numbers(n, frst, last):
    return [randint(frst, last) for i in range(n)]


def pairs_prod(numbers):
    results = []
    while len(numbers) > 1:
        results.append(numbers[0] * numbers[-1])
        del numbers[0]
        del numbers[-1]
    if len(numbers) == 1:
        results.append(numbers[0] ** 2)
    return results


n = 9
frst = 1
last = 10

my_list = get_numbers(n, frst, last)
print(my_list)
print(pairs_prod(my_list))
