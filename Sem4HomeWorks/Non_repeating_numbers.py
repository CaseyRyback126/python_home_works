# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# Пример: - Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]

from random import randint


size = 10
m = 1
n = 10

lst = [randint(m, n) for i in range(size)]
print(lst)
lst_sort = []
for i in lst:
    if lst.count(i) < 2:
        lst_sort.append(i)
print(lst_sort)
