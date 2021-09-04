# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def sort_merge(array):
    if len(array) <= 1:
        return array

    left_side = sort_merge(array[:len(array) // 2])
    right_side = sort_merge(array[len(array) // 2:])

    i = j = 0
    result = []

    while i < len(left_side) or j < len(right_side):

        if i >= len(left_side):
            result.append(right_side[j])
            j += 1

        elif j >= len(right_side):
            result.append(left_side[i])
            i += 1

        elif left_side[i] < right_side[j]:
            result.append(left_side[i])
            i += 1

        else:
            result.append(right_side[j])
            j += 1

    return result


elements = [random.uniform(0, 50) for _ in range(15)]

print(f'Исходный массив: {elements}')
print(f'Отсортированный массив: {sort_merge(elements)}')
