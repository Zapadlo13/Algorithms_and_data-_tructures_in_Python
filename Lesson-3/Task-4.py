# 4. Определить, какое число в массиве встречается чаще всего.

import random

elements = [random.randint(1, 15) for _ in range(20)]

a = {}
print(f'Исходный массив: {elements}')

for el in elements:

    if a.get(el) == None:
        a[el] = 1
    else:
        a[el] += 1

max_key = []
max_num = 0

for key in a:
    if a[key] > max_num:
        max_num = a[key]
        max_key = [key]
    elif a[key] == max_num:
        max_key.append(key)

print(f'Числа: {max_key} встречаются по {max_num} раза.')
