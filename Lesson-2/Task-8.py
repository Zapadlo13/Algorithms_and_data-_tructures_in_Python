# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

num1 = input('Введетие последовательность цифр:')
num2 = input('Введетие цифры для посика:')

count = 0
while True:

    if num1.find(num2) >=0:
        count += 1
        num1 = num1[num1.find(num2)+len(num2):]
    else:
        break
print(f'Цифра {num2} встречавется {count} раз.')