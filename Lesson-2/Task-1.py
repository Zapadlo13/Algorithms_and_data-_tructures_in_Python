# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

def get_float(number):
    return float(number.replace(',', '.'))


def get_numbers(expression, symbol):
    f = expression.find(symbol)
    a = get_float(expression[:f])
    b = get_float(expression[f + 1:])
    return a, b


while True:
    expression = input('Введите выражение или 0 для выхода ')
    rezult = 0
    if expression == '0':
        break
    elif expression.find('+') > 0:
        a, b = get_numbers(expression, '+')
        rezult = a + b
    elif expression.find('-') > 0:
        a, b = get_numbers(expression, '-')
        rezult = a - b
    elif expression.find('*') > 0:
        a, b = get_numbers(expression, '*')
        rezult = a * b
    elif expression.find('/') > 0:
        a, b = get_numbers(expression, '/')
        if b == 0:
            print('На ноль дельть нельзя!')
            continue
        rezult = a / b
    else:
        print('Операция не распознана! Попробуйте еще раз.')
        continue

    print(f'Результат: {round(rezult, 2)}')
