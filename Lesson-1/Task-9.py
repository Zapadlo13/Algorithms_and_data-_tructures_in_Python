# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = float(input('Введите число a: '))
b = float(input('Введите число b: '))
c = float(input('Введите число c: '))

# Способ 1
if (a > b and a < c) or (a < b and a > c):
    mid = a
elif (b > a and b < c) or (b < a and b > c):
    mid = b
else:
    mid = c

print(f'Среднее число {mid}')

# Способ 2
max_int = max(a, b, c)
min_int = min(a, b, c)

if a > min_int and a < max_int:
    mid = a
elif b > min_int and b < max_int:
    mid = b
else:
    mid = c

print(f'Среднее число {mid}')

# Способ 3
mid = a + b + c - max(a, b, c) - min(a, b, c)

print(f'Среднее число {mid}')
