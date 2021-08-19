# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

elements = [random.randint(1, 25) for _ in range(15)]

print(f'Исходный массив: {elements}')

min_el = min(elements)
max_el = max(elements)

for key, el in enumerate(elements[:]):
    if el == min_el:
        elements[key] = max_el
    if el == max_el:
        elements[key] = min_el

print(f'Минимальный элемент: {min_el}, максимальный элемент: {max_el}')
print(f'Обработанный массив: {elements}')
