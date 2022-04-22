# Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел
import os
os.system('cls')
import datetime

def rand_number():
    return datetime.datetime.now().microsecond % 10 # выдает дату часы минуты секунды микросекунды сейчас

rand = rand_number()
print(f'Random number is: {rand}')