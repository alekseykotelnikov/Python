# Составить список простых множителей натурального числа N
import os
os.system("cls")

n = int(input('Введите число: '))
def prime_number (n):
    i = 2
    array = []
    while n != 1: 
        if n % i == 0:
            array.append(i) 
            n = n / i
            i = 2
        else: 
            i += 1
    return (array)
array = prime_number(n)
print(f'Список простых множителей натурального числа {n} = {array}')