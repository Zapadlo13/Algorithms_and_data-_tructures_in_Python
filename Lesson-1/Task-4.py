# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

import random
import string

ll = int(input('Нижная граница случайного целого числа: '))
ul = int(input('Верхная граница случайного целого числа: '))

print(f'Случайное целое число: {random.randint(ll, ul)}')

ll = float(input('Нижная граница случайного вещественное числа: '))
ul = float(input('Верхная граница случайного вещественное числа: '))

print(f'Случайное вещественное число: {random.uniform(ll, ul)}')

ll = input('Нижная граница случайного символа: ')
ul = input('Верхная граница случайного символа : ')

print(
    f'Случайный символ : {string.ascii_letters[random.randint(string.ascii_letters.find(ll), string.ascii_letters.find(ul))]}')
