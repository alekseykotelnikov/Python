# Реализовать алгоритм перемешивания списка
import os
os.system('cls')
import random

def get_list():
    list = []
    for i in range(1, 50, 6): # выдать числа от 1 до 50 с шагом  6
        list.append(i)
    return list

def rnd_shuffle(list):
    return random.shuffle(list)
    

list = get_list()
print(f'We have next list: {list}')
rnd_shuffle(list)
print(f'shuffle list is: {list}')