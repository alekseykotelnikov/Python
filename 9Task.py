# Указав номер четверти прямоугольной системы координат, 
# показать допустимые значения координат для точек этой четверти
import os
from unittest import result
os.system("cls")

from random import randint
num = randint(1, 4)
print(f'Номер четверти прямоугольной системы координат, это: {num}')

def PrintCoords(num):
    if num == 1:
        result = 'x > 0, y > 0'
    elif num == 2:
        result = 'x < 0, y > 0'
    elif num == 3:
        result = 'x < 0, y < 0'
    else:
        result = 'x > 0, y < 0'
    return result

coords = PrintCoords(num)
print(f'Допустимые значения координат для точек этой четверти, это: {coords}')