# Определить, присутствует ли в заданном списке строк, некоторое число
import os
os.system('cls')

list = ['kfj1', 'fgf22', 76, 98, 11]
number = str(input('Enter number: '))

list = str(list)
result = list.find(number) # проверяем есть ли символ в строке, если нет то значение = -1
print(result)
if result >= 0:
    print('Number is on the list')
else:
    print('Number is not on the list')