# Подсчитать сумму цифр в вещественном числе.
import os
os.system('cls')

def try_parse_float():
    while True:
        try:
            console_input = float(input('Enter the number: '))
            return console_input
        except ValueError:
            print('Wrong number. Try again')


n = try_parse_float()
n = str(n)
n = (n.replace('.', ''))
n = list(n)
result = sum(map(int, n))
print(n)
print(result)

