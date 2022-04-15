# Вывести на экран числа от -N до N
import os
os.system("cls")

number = int(input('Введите число N: '))
for i in range(-number, number + 1):
    print(i, end=' ')