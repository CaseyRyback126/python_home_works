# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


from random import randint

with open('positions.txt', 'w') as data:
    data.write('0\n')
    data.write('3\n')
    data.write('5\n')
    data.write('8\n')
    data.write('10\n')


def get_numbers(n):
    return [randint(-n / 2, n) for i in range(-n, n + 1)]


def get_data_from_file(path):
    data = open(path, 'r')
    dlist = [int(line.strip()) for line in data]
    data.close()
    return dlist


def get_prod(numbers, datalist):
    prod = 1
    for i in datalist:
        prod *= numbers[i]
    return prod


path = 'positions.txt'
n = 10
datalist = get_data_from_file(path)
numbers = get_numbers(n)

print(numbers)
print(datalist)
print(get_prod(numbers, datalist))
