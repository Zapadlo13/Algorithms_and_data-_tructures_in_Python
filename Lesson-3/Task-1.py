# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

a = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for el in range(2, 100):
    for key in a:
        if el % key == 0:
            a[key] += 1

for key in a:
    print(f'Числу {key} кратно {a[key]} чисел')