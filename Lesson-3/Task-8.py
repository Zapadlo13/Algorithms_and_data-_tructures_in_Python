#8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

import random

elements = []
for _ in range(5):
    elements.append([random.randint(-15, 15) for _ in range(3)])

for el in elements:
    el.append(sum(el))
    print(el)