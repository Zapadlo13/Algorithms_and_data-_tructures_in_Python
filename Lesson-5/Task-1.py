# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections

companies = collections.defaultdict(list)

n = int(input('Введите кол-во компаний: '))
total_profit = 0
for i in range(n):
    name = input(f'Введите наименование {i + 1}-ой компании: ')
    profit = []
    for month in range(4):
        profit.append(float(input(f'Введите прибыль за {month + 1}-ый квартал: ')))
        total_profit += profit[month]

    companies[name].append(profit)

avg = total_profit / n

print(f'Средная прибыль по компаниям: {round(avg, 2)}')
print('Наименования предприятий, чья прибыль выше среднего:')
for comp in companies:
    if sum(companies[comp][0]) > avg:
        print(comp)

print('Наименования предприятий, чья прибыль ниже среднего:')
for comp in companies:
    if sum(companies[comp][0]) < avg:
        print(comp)
