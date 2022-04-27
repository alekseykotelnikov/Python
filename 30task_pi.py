# 30. Вычислить число pi c заданной точностью d
# Пример: при d = 0.001,  pi = 3.142. 10**-1 <= d10 <= 10**-10
import os
from math import *
os.system("cls")

print(f'Число Пи: {pi}')
num = int(input('Введите какое количество знаков после запятой нужно выводить: '))
d = 10**(-num)
print(f'Точность d = {d}')
a = (floor(pi * 10**num)) / 10**num
print(f'Пи = {a}')