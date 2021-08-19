# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

elements = [random.randint(-15, 15) for _ in range(10)]

a = {}
print(f'Исходный массив: {elements}')

max_el = min(elements)
max_key = 0

for key, el in enumerate(elements):
    if el < 0 and max_el <= el:
        max_el = el
        max_key = key

print(f'Саксимальный отрицательный элемент: {max_el}  на позиции: {max_key}')
