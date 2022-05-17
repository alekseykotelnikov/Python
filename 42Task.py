# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные данные:
# 12W1B12W3B24W1B14W

import os
os.system('cls')

def encode_file(my_text):  
    str_code = ''
    count = 1       
    for i in range(len(my_text)):
        if i < len(my_text)-1:
            if my_text[i] == my_text[i + 1]:
                count += 1
            else:
                str_code += str(count) + my_text[i]
                count = 1
        else:
            str_code += str(count) + my_text[i]
    return str_code



def decode_file(strc):
    count = ''
    result = ''
    for i in strc:
        if i.isdigit():
            count += i
        else:
            result += i * int(count)
            count = ''
    return result

text = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
print(f'Предоставлен следующий текст: \n{text}')
with open('42_decode.txt', 'w') as data:
    data.write(text)

with open('42_decode.txt', 'r') as data:
    my_text = data.read()

strc = encode_file(my_text)
print(f'Сжатый текст будет вот такого вида: \n{strc}') # Проверка магии

with open('42_code2.txt', 'w') as data:
    data.write(strc)

with open('42_code2.txt', 'r') as data:
    my_text = data.read()

total = decode_file(my_text)
print(f'Восстановленный текст будет следующего вида: \n{total}') # проверка второй магии

with open('42_decode.txt', 'w') as data:
    data.write(total)