# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
import os
os.system("cls")

number = int(input('Введите число от 1 до 7: '))
if 1 <= number <= 7:
    if number == 1:
        print('Monday')
        print('Не выходной')
    elif number == 2:
        print('Tuesday')
        print('Не выходной')
    elif number == 3:
        print('Wednesday') 
        print('Не выходной')       
    elif number == 4:
        print('Thursday')
        print('Не выходной')
    elif number == 5:
        print('Friday')
        print('Не выходной')
    elif number == 6:
        print('Saturday')
        print('Выходной')
    elif number == 7:
        print('Sunday')
        print('Выходной')
else:
    print('Введено ошибочное число')