# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
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
    from random import randint
    mylist = []
    for i in range(n):
        mylist.append(randint(-10, 10))
    return mylist


n = try_parse_int()
the_list = get_list(n)

print('Сформированный список будет следующим: {}'.format(the_list))

for i in the_list:
    print(i, end=' ')