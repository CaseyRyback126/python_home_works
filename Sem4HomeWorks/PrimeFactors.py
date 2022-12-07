# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.


n = int(input('Введите число: '))
def prime_factor (n):
    i = 2
    fact_list = []
    while n != 1:
        if n % i == 0:
            fact_list.append(i)
            n = n / i
            i = 2
        else:
            i += 1
    return (fact_list)

print (prime_factor (n))
