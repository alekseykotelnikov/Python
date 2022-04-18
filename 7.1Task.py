# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
from unittest import result


def logic(x, y, z):
    if (not (x or y or z) == (not x and not y and not z)):
        result = True
    else:
        result = False
    print(result)
    return result

f1 = logic(True, True, True)
f2 = logic(True, True, False)
f3 = logic(True, False, True)
f4 = logic(False, True, True)
f5 = logic(True, False, False)
f6 = logic(False, False, True)
f7 = logic(False, True, False)
f8 = logic(False, False, False)

if (all([f1, f2, f3, f4, f5, f6, f7, f8])) == True:
    print('Выражение тождественно')
else:
    print('Выражение НЕ тождественно')
