# В заданном списке вещественных чисел найдите разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
from random import *
os.system("cls")

list = [1.1, 1.2, 3.1, 5, 10.01]  # [uniform(1, 21) for i in range(8)]
print(list, '\n')
list1 = []

for i in range(len(list)):
    if list[i] - round(list[i]) == 0:
        continue
    else:

        list1.append(round(list[i] - round(list[i]), 3))

print(list1)
print('\nМаксимальное число: ', max(list1))
print('\nМинимальное число: ', min(list1))
print('\nРазница: ', max(list1) - min(list1))
