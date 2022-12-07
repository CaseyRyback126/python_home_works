# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100)* многочлена
# и записать в файл многочлен степени k.
# *Пример:*
#             k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#             k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0

from random import randint
import itertools

k = randint(2, 7)


def get_coef(k):
    coef = [randint(0, 10) for i in range(k + 1)]
    while coef[0] == 0:
        coef[0] = randint(1, 10)
    return coef


def get_polynomial(k, coef):
    var = ['*x^'] * (k - 1) + ['*x']
    polynom = [[a, b, c] for a, b, c in itertools.zip_longest(coef, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynom:
        x.append(' + ')
    polynom = list(itertools.chain(*polynom))
    polynom[-1] = ' = 0'
    return "".join(map(str, polynom)).replace(' 1*x', ' x')


coef = get_coef(k)
polynom1 = get_polynomial(k, coef)
print(polynom1)

with open('Polinom_1.txt', 'w') as data:
    data.write(polynom1)

# Второй многочлен для следующей задачи:

k = randint(2, 5)

coef = get_coef(k)
polynom2 = get_polynomial(k, coef)
print(polynom2)

with open('Polinom_2.txt', 'w') as data:
    data.write(polynom2)
