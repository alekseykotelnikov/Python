# Пользователь задаёт две строки. 
# Определить количество вхождений одной строки в другой.
import os
os.system('cls')

def number_of_intersection(str1, str2):
    str1 = set(str1)
    str2 = set(str2)
    result = (str1.intersection(str2))
    result = list(result)
    count = 0
    for i in result:
        count += 1
    return count



str1 = str(input('Enter String One:'))
str2 = str(input('Enter String Two:'))

print('Number of count in {} and {} is: '.format(str1, str2))
count = number_of_intersection(str1, str2)
print(count)