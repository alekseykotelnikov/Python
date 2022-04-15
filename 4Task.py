# Показать первую цифру дробной части числа
import os
os.system("cls")

from random import uniform
number = uniform(1, 3)
print('Дано число: ', number)

first_digit = int(number * 10) % 10
print('Первая цифра числа, это: ', first_digit)