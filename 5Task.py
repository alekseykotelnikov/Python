# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
import os
os.system("cls")

number = int(input('Введите число: '))

if (number % 5 == 0 and number % 10 == 0) or (number % 15 == 0 and number % 30 != 0):
    print('Проверка числа успешна')
else:
    print('Чсило не подходит под условия')