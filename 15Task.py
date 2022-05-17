# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

import os
os.system('cls')
from itertools import *
import operator
from random import *
# def try_parse_int():
#     while True:
#         try:
#             console_input = int(input('Enter the N number: '))
#             if 3 <= console_input <= 8:
#                 return int(console_input)
#         except ValueError:
#             print('Wrong number. Try again')

# def factorial(n):
#     list = [1]
#     for i in range(2, n + 1):
#         list.append(i * list[i - 2])
#     return list

# n = try_parse_int()
# list = factorial(n)
# print(list)

n = randint(4, 9)
print(*list(accumulate([x for x in range(1, n + 1)], operator.mul)))



