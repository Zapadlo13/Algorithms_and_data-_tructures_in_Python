#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

from functools import reduce

def get_sum_numbers(num):
    a = list(map(int, list(num)))

    return reduce(lambda x, y: x + y, a)


max_num =0
max_sum =0
while True:
    num = input('Введите число или 0 для выхода: ')
    if num == '0':
        break
    sum = get_sum_numbers(num)
    if max_sum<sum:
        max_sum = sum
        max_num = num

print(f'Наибольшая сумма цифр: {max_sum} в числе {max_num}.')