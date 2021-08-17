# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

def get_list_numbers(num):
    l = [1]
    i = 1
    for r in range(num - 1):
        i /= 2
        if r % 2 == 0:
            l.append(-i)
        else:
            l.append(i)
    return l


num = int(input('Введиет кол-во элементов: '))
l = get_list_numbers(num)
print(f'Ряд числе {l} сумма {sum(l)}')
