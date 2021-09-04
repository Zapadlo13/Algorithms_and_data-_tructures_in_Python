#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random

def sort_bool(array,revers):
    n = 1
    while n < len(array)+1:
        for i in range(len(array) - n):
            if revers:
                if array[i] < array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
            else:
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


elements = [random.randint(-100, 100) for _ in range(15)]

print(f'Исходный массив: {elements}')
print(f'Отсортированный массив: {sort_bool(elements,False)}')
print(f'Отсортированный массив реверс: {sort_bool(elements,True)}')
