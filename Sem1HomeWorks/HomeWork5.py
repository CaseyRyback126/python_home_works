# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример: - A (3,6); B (2,1) -> 5,09
#         - A (7,-5); B (1,-1) -> 7,21
import math
from random import randint


def Get_coordinates(num_axis, left, right):  # координаты точек
    return tuple([randint(left, right) for i in range(num_axis)])


def Find_dist(a, b):  # расстояние между точками
    return round(math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b))), 3)


num_axis = 2  # количество осей координат
left = -10
right = 10

point_A = Get_coordinates(num_axis, left, right)
point_B = Get_coordinates(num_axis, left, right)

print(f'A {point_A}, B {point_B}')
print(f'Расстояние между точками: {Find_dist(point_A, point_B)}')
