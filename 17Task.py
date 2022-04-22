# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число
from random import randint
import os
os.system('cls')

def try_parse_int():
    while True:
        try:
            console_input = int(input('Enter the N number: '))
            if 3 <= console_input <= 8:
                return int(console_input)
        except ValueError:
            print('Wrong number. Try again')

def get_list(n):
    return [randint(-n, n) for i in range(n)]

def get_position():
    path = '17Task.txt'
    data = open(path, 'r')
    list2 = []
    for line in data:
        list2.append(int(line))
    return list2

n = try_parse_int()

with open('17Task.txt', 'a') as data:
    data.writelines(f'{randint(1, n) - 1}\n') # -1 так как это индекс, должен быть меньше 
    data.writelines(f'{randint(1, n) - 1}\n') # чем количество чисел в первом списке
    data.writelines(f'{randint(1, n) - 1}')

def get_multi(list, list2):
    result = 1
    for i in list2:
        result *= list[i]
    return result

list2 = get_position()
list = get_list(n)
data.close()
multi = get_multi(list, list2)
print(f'We have next list: {list}')
print(f'We have next position: {list2}')
print(f'Multiplication is: {multi}')