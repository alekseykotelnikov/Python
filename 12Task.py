# Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.

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



def get_dictionary(n):
    print('Для натурального N словарь индекс-значение, ', end="")
    print('состоящий из элементов последовательности 3n + 1, будет: ')
    return {a: 3 * a + 1 for a in range(1, n + 1)}

n = try_parse_int()
print(get_dictionary(n))