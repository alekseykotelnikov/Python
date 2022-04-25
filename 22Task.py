# Задача 22
# Найти сумму чисел списка стоящих на нечетной позиции
import random


spisok =[]
a = int(input("Введите длину списка :"))
for i in range(a):
    spisok.append(random.randint(1,10))
print(f"Создан новый список: \n {spisok}")
sum = 0
for i in range(a):
    if i % 2 > 0: sum += spisok[i]
print(f"Сумма чисел списка стоящих в нечетных позициях = {sum}")
