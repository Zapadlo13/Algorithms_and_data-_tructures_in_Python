# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
import string

number = int(input('Введите номер буквы в алфавите от 1 до 26: '))

print(f'Под номером {number} в алфавите буква: {string.ascii_letters[number - 1]}')
