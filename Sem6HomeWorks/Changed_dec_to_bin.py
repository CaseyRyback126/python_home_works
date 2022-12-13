# Напишите программу, которая будет преобразовывать десятичное число в двоичное
# Пример: 45 -> 101101


# Было

print("Введите десятичное число для преобразования в двоичное ")
number = int(input())
binar_number = ''

while number // 2 != 0:
    binar_number += str(number % 2)
    number = number // 2

binar_number += '1'
print(binar_number[:: -1])

# Стало

n = int(input('Введите число: '))
print(bin(n).replace('0b', ''))
