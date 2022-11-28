# Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.
# (Не используя библиотеки связанные с рандомом)

import datetime

min_n = 10
max_n = 100


def get_rand(a, b):
    rand = datetime.datetime.now().microsecond % 10 + (max_n // (min_n + 3)) + min_n
    return rand


n = get_rand(min_n, max_n)

print(n)
