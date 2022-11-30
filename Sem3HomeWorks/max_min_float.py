# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19

from random import uniform


def get_float_nums(n, first, last):
    return [round(uniform(first, last), 2) for i in range(n)]


def find_diff(my_nums):
    nums = [round(x - int(x), 2) for x in (my_nums)]
    return max(nums) - min(nums)


n = 5
first = 1
last = 10
my_nums = get_float_nums(n, first, last)

print(my_nums)
print(find_diff(my_nums))
