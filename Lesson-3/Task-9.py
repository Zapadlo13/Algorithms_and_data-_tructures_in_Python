# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

elements = []
for _ in range(5):
    elements.append([random.randint(-15, 15) for _ in range(5)])

print(f'Исходный массив 5*5: {elements}')

max_el = []
for inx in range(len(elements[0])):
    min_el = []
    for el in elements:
        min_el.append(el[inx])

    max_el.append(min(min_el))

print(f'Минимальные элементы столбцов: {max_el}')
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max(max_el)}')
