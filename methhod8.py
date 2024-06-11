# Заданные данные в виде таблицы (x, f(x))
table1 = [
 [2.4, 3.526],
 [2.6, 3.782],
 [2.8, 3.945],
 [3.0, 4.043],
 [3.2, 4.104],
 [3.4, 4.155],
 [3.6, 4.222],
 [3.8, 4.331],
 [4.0, 4.507],
 [4.2, 4.775],
 [4.4, 5.159],
 [4.6, 5.683],
]
x_vtockax = [2.55, 3.21, 4.32, 3.92]

# Функция для вычисления интерполяционного полинома Лагранжа в точке x
def Lagrang(table, x_target):
    # Вычисляем шаг h (разницу между значениями x)
    h = table1[1][0] - table1[0][0]

    # Найдем индекс ближайшей точки слева от x_target
    index = next(i for i, (x, _) in enumerate(table1) if x >= x_target) - 1

    if index < 1 or index + 1 >= len(table1):
        # Если значение x_target находится за пределами заданных данных, возвращаем сообщение об ошибке
        return f"Для x_target={x_target}: Значение x_target находится за пределами заданных данных или не достаточно точек слева для вычисления производной."
    else:
        # Используем формулу для численного дифференцирования на основе полиномов Лагранжа
        diff = (table1[index + 1][1] - table1[index - 1][1]) / (2 * h) - (h ** 2 / 6) * table1[index][1]
        return f"y'({x_target}) = {diff}"

# Функция для вычисления производной с использованием метода Ньютона
def Newton(table1, x_vtockax):
    results = []
    for x_target in x_vtockax:
        # Вычисляем шаг h (разницу между значениями x)
        h = table1[1][0] - table1[0][0]

        # Найдем индекс ближайшей точки слева от x_target
        index = next(i for i, (x, _) in enumerate(table1) if x >= x_target) - 1
        if index < 0 or index + 1 >= len(table1):
            # Если нет данных для вычисления производной, добавляем сообщение об ошибке в результаты
            results.append(f"Для x_target={x_target}: Нет данных для вычисления производной.")
        else:
            # В противном случае вычисляем производную по методу Ньютона
            diff = (table1[index + 1][1] - table1[index][1]) / h
            results.append(f"y'({x_target}) = {diff}")
    return results

# Вычисление и вывод результатов для метода Лагранжа
print('Вычисление и вывод результатов для метода Лагранжа')
for x_target in x_vtockax:
    result = Lagrang(table1, x_target)
    print(result)

# Вычисление и вывод результатов для метода Ньютона
print('Вычисление и вывод результатов для метода Ньютона')
results2 = Newton(table1, x_vtockax)
for result in results2:
    print(result)






table1 = [
 [2.4, 3.526],
 [2.6, 3.782],
 [2.8, 3.945],
 [3.0, 4.043],
 [3.2, 4.104],
 [3.4, 4.155],
 [3.6, 4.222],
 [3.8, 4.331],
 [4.0, 4.507],
 [4.2, 4.775],
 [4.4, 5.159],
 [4.6, 5.683],
]
x_vtockax = [2.55, 3.21, 4.32, 3.92]
def Lagrang(table, x_target):
    h = table1[1][0] - table1[0][0]
    index = next(i for i, (x, _) in enumerate(table1) if x >= x_target) - 1

    if index < 1 or index + 1 >= len(table1):
        return f"Для x_target={x_target}: Значение x_target находится за пределами заданных данных или не достаточно точек слева для вычисления производной."
    else:
        diff = (table1[index + 1][1] - table1[index - 1][1]) / (2 * h) - (h ** 2 / 6) * table1[index][1]
        return f"y'({x_target}) = {diff}"
def Newton(table1, x_vtockax):
    results = []
    for x_target in x_vtockax:
        h = table1[1][0] - table1[0][0]
        index = next(i for i, (x, _) in enumerate(table1) if x >= x_target) - 1
        if index < 0 or index + 1 >= len(table1):
            results.append(f"Для x_target={x_target}: Нет данных для вычисления производной.")
        else:
            diff = (table1[index + 1][1] - table1[index][1]) / h
            results.append(f"y'({x_target}) = {diff}")
    return results
print('Вычисление и вывод результатов для метода Лагранжа')
for x_target in x_vtockax:
    result = Lagrang(table1, x_target)
    print(result)
print('Вычисление и вывод результатов для метода Ньютона')
results2 = Newton(table1, x_vtockax)
for result in results2:
    print(result)