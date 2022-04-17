# Найти расстояние между двумя точками пространства
import math
import os
os.system("cls")

from random import randint
x1, y1, z1 = randint(1, 10), randint(1, 10), randint(1, 10)
x2, y2, z2 = randint(11, 20), randint(11, 20), randint(11, 20)
print('Даны координаты двух точек в трехмерном пространсвте:')
print(f'x1 = {x1}, y1 = {y1}, z1 = {z1} и x2 = {x2}, y2 = {y2}, z2 = {z2}')

def DistanceCoords(x1, x2, y1, y2, z1, z2):
    result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return result

distance = DistanceCoords(x1, x2, y1, y2, z1, z2)
print(f'Расстояние между двумя точками пространства = {distance}')