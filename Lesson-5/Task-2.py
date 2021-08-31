# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import collections

HEX_STR = '0123456789ABCDEF'


def get_num(lst):
    try:
        return lst.pop()
    except:
        return ''


class HexNumber:
    def __init__(self, number):
        self.number = list(number.upper())

    def __str__(self):
        return f'{self.number}'

    def __add__(self, obj):
        a = self.number.copy()
        b = obj.number.copy()

        max_len = max(len(a), len(b))

        answer = collections.deque()

        temp = 0
        for _ in range(max_len):
            c = HEX_STR.find(get_num(a)) + HEX_STR.find(get_num(b)) + temp
            temp = c // 16
            answer.appendleft(HEX_STR[c % 16])

        return answer

    def __mul__(self, obj):
        a = int(''.join(self.number), 16)
        b = int(''.join(obj.number), 16)

        answer = HexNumber(hex(a * b))

        return answer


# a =  HexNumber(input('Введите первое 16-ти значное число: '))
# b =  HexNumber(input('Введите первое 16-ти значное число: '))

a = HexNumber('a2')
b = HexNumber('c4f')

print(a, b)
print(f'{a} + {b} = {a + b}')
print(f'{a} * {b} = {a * b}')
