#5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

import string

a = input('Введите первую букву: ')
b = input('Введите вторую букву: ')

print(f'Буква {a} в алфавите под номером {string.ascii_letters.find(a)+1}')
print(f'Буква {b} в алфавите под номером {string.ascii_letters.find(b)+1}')

print(f'Между ними находится  {string.ascii_letters.find(b)-string.ascii_letters.find(a)}')