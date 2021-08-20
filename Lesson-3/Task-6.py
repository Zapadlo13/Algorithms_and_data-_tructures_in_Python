# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

elements = [random.randint(-15, 15) for _ in range(15)]

print(f'Исходный массив: {elements}')

min_inx = elements.index(min(elements))
max_inx = elements.index(max(elements))

print(f'Массив между min и max: {elements[min(min_inx, max_inx) + 1:max(min_inx, max_inx)]}')
print(f'Сумма между min и max: {sum(elements[min(min_inx, max_inx) + 1:max(min_inx, max_inx)])}')
