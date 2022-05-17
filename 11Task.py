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
def get_degree(n):
    print('Список из {} членов последовательности, будет: '.format(n))
    return [((-3)**i) for i in range(n)]

print(list((-3)**i for i in range(int(input()))))

n = try_parse_int()
print(get_degree(n))
