# задать список из n чисел последовательности (1+〖1/n)〗^n и вывести на экран их сумму

import os
import random
os.system("cls")

n = random.randint(6, 16)
# print(n)
# n = 8
# massive = []

# for i in range(1, n+1):
#     massive.append(1+(1/i)**i)
# print(f'{sum(massive):.2f}')
# number = [(1+(1/i)**i) for i in range(1, n+1)]
print(f'{sum([(1+(1/i)**i) for i in range(1, n+1)]):.2f}')