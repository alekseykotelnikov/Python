import os
os.system('cls')
from itertools import *
import operator
from random import *

# def multy(a):
#     if a == 1:
#         return 1
    
#     return a * multy(a-1)

# n = 10

# print("Sequence for ")
# for i in range(1, n+1):
#     print(multy(i), end=' ')

n = randint(4, 9)
print(*list(accumulate([x for x in range(1, n + 1)], operator.mul)))