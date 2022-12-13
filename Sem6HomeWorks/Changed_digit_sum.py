# №1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#  Пример:  6782 -> 23; 0.56 -> 11

print("Введите вещественное число\n")
str = input()
#               БЫЛО:
summa = 0
number = []
for i in range(len(str)):
    if str[i].isdigit():
        summa += int(str[i])
print("Сумма цифр числа = ", summa)

#              СТАЛО:

number = str.replace('.', '')
number = [int(i) for i in number]
print("Сумма цифр числа = ", sum(number))
