# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.(Сделать для строки)
# *Пример:*    - 6782 -> 23
#              - 0,56 -> 11

from random import uniform

num = round(uniform(1, 100), 3)


def sum_digit(n):
    return sum(map(int, list(str(n).replace('.', ''))))


print(num)
print(sum_digit(num))
