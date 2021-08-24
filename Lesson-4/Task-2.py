# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
import cProfile


def without_sieve(n):
    lst = []
    k = 0
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            lst.append(i)
        else:
            k = 0
    print(lst)


def sieve(n):
    a = list(range(n + 1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    print(lst)


cProfile.run('without_sieve(1000)')  # 173 function calls in 0.044 seconds
cProfile.run('sieve (1000)')  # 173 function calls in 0.000 seconds

cProfile.run('without_sieve(10000)')  # 1234 function calls in 3.922 seconds
cProfile.run('sieve (10000)')  # 1234 function calls in 0.007 seconds

cProfile.run('without_sieve(100000)')  # 9597 function calls in 394.024 seconds
cProfile.run('sieve (100000)')  # 9597 function calls in 0.049 seconds

# Функция без использования решета  очень сильно  проигрывает  решету.
