# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
import cProfile


def create_arrya(n):
    elements = []
    for _ in range(n):
        elements.append([random.randint(-1500, 1500) for _ in range(n)])
    return elements


def arrya(elements):
    max_el = []
    for inx in range(len(elements[0])):
        min_el = []
        for el in elements:
            min_el.append(el[inx])

        max_el.append(min(min_el))

    print(f'Минимальные элементы столбцов: {max_el}')
    print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max(max_el)}')


def arrya2(elements):
    max_el = min(elements[0])
    for inx in range(len(elements[0])):
        min_el = elements[0][inx]
        for el in elements:
            if min_el > el[inx]:
                min_el = el[inx]
        if max_el < min_el:
            max_el = min_el

    print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_el}')


elements = create_arrya(50)
cProfile.run('arrya(elements)')  # 2608 function calls in 0.001 seconds
cProfile.run('arrya2(elements)')  # 7 function calls in 0.000 seconds

elements = create_arrya(500)
cProfile.run('arrya(elements)')  # 251008 function calls in 0.080 seconds
cProfile.run('arrya2(elements)')  # 7 function calls in 0.019 seconds

elements = create_arrya(5000)
cProfile.run('arrya(elements)')  # 25010008 function calls in 15.613 seconds
cProfile.run('arrya2(elements)')  # 7 function calls in 5.260 seconds

# Убрав из своего решения 2 списка, удалось сильно увеличь производительность как по времени так и по памяти.
# cProfile показывает  методы, сколько раз были вызваны и сколько времени они заняли.
# В такой же работе в 1С я привык  что при оценке времени работы видно каждую строку кода,
# сколько она раз исполнялась и сколько времени она заняла, если ли что-то подобное в Python?
