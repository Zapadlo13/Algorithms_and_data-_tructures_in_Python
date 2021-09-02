# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

import random
from pympler import tracker


def create_arrya(n):
    elements = []
    for _ in range(n):
        elements.append([random.randint(-1500, 1500) for _ in range(n)])
    return elements


tr = tracker.SummaryTracker()


def arrya(elements):
    max_el = []
    for inx in range(len(elements[0])):
        min_el = []
        for el in elements:
            min_el.append(el[inx])

        max_el.append(min(min_el))

    print(f'Минимальные элементы столбцов: {max_el}')
    print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max(max_el)}')


tr.print_diff()

tr = tracker.SummaryTracker()


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


tr.print_diff()

elements = create_arrya(1000)
arrya(elements)
#               types |   # objects |   total size
# ======================= | =========== | ============
#                    list |        3357 |    291.62 KB
#                     str |        3354 |    233.14 KB
#                     int |         756 |     20.68 KB
#                    dict |           3 |    400     B
#                    code |           1 |    246     B
#   function (store_info) |           1 |    136     B
#        function (arrya) |           1 |    136     B
#                    cell |           2 |     80     B
#                 weakref |           1 |     72     B
#                  method |           1 |     64     B
#                   tuple |           1 |      8     B
arrya2(elements)
# ================================ | =========== | ============
#                             code |           2 |    352     B
#                             dict |           1 |    232     B
#            function (store_info) |           1 |    136     B
#                function (arrya2) |           1 |    136     B
#                              str |           1 |     87     B
#                             cell |           2 |     80     B
#                           method |           1 |     64     B
#                            tuple |           1 |     56     B
#                             list |           0 |      8     B
#   pympler.tracker.SummaryTracker |          -1 |    -48     B

# При подсчете  двух алгоритмов  нахождения максимального элемента среди минимальных элементов столбцов матрицы.
# Видно что алгоритм где используется строковая переменная вместо списка намного предпочтительней.
