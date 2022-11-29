# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#  Пример:  - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint


def get_list(n, first, last):
    return [randint(first, last) for i in range(10)]


def sum_odds(my_list):
    return sum(my_list[1::2])


first = 1
last = 10

my_list = get_list(10, first, last)
print(my_list)
print(sum_odds(my_list))
