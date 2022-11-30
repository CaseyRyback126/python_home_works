# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так:
#       [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))


def get_negafibonacci(n):
    fibo = []
    a, b = 1, 1
    for i in range(n):
        fibo.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(n + 1):
        fibo.insert(0, a)
        a, b = b, a - b
    return fibo


fibo_nums = get_negafibonacci(n)
print(get_negafibonacci(n))
print(fibo_nums.index(0))
