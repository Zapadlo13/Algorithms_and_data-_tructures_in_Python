# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
from functools import reduce

a = list(map(int, list(input('Введите трехзначное число: '))))

summa = reduce(lambda x, y: x + y, a)
print(f'Сумма цифр трехзначного числа: {summa}')
multiplication = reduce(lambda x, y: x * y, a)
print(f'Произведение цифр трехзначного числа: {multiplication}')
