class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

def Lagrange(points, x):
    lagrangePol = 0

    for i in range(len(points)):
        basicsPol = 1

        for j in range(len(points)):
            if j != i:
                basicsPol *= (x - points[j].X) / (points[i].X - points[j].X)

        lagrangePol += basicsPol * points[i].Y

    return lagrangePol

def Newton1(points, x):
    n = len(points)
    y = [[0]*n for _ in range(n)]

    for i in range(n):
        y[i][0] = points[i].Y

    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

    sum = y[0][0]
    t = (x - points[0].X) / (points[1].X - points[0].X)
    chils = t
    znam = 1

    for i in range(1, n):
        znam *= i
        sum += (chils * y[0][i]) / znam
        chils *= (t - i)

    return sum

def Newton2(points, x):
    n = len(points)
    y = [[0]*n for _ in range(n)]

    for i in range(n):
        y[i][0] = points[i].Y

    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            y[j][i] = y[j][i - 1] - y[j - 1][i - 1]

    sum = y[n - 1][0]
    t = (x - points[n - 1].X) / (points[1].X - points[0].X)
    chils = t
    znam = 1

    for i in range(1, n):
        znam *= i
        sum += (chils * y[n - 1][i]) / znam
        chils *= (t + i)

    return sum

def Print(points, x, title, interpolate):
    print("Исходные точки: ")
    for i in range(len(points)):
        print(f"{points[i].X:.3f}\t{points[i].Y:.5f}")

    print(f"\n{title}:")
    for i in range(len(x)):
        result = interpolate(points, x[i])
        print(f"{x[i]:.3f}\t{result:.5f}")

    print("------------------------------------")

def Print1(points, x, interpolate1, interpolate2):
    print("Исходные точки: ")
    for i in range(len(points)):
        print(f"{points[i].X:.3f}\t{points[i].Y:.5f}")

    for i in range(len(x)):
        if x[i] - points[0].X < points[-1].X - x[i]:
            result = interpolate1(points, x[i])
            title = 'Первая интерполяционная формула Ньютона:'
        else:
            result = interpolate2(points, x[i])
            title = 'Вторая интерполяционная формула Ньютона:'
        print(f"\n{title}")
        print(f"{x[i]:.3f}\t{result:.5f}")

    print("------------------------------------")

def Main():
    points1 = [
        Point(0.68, 0.8086),
        Point(0.73, 0.8949),
        Point(0.80, 1.0296),
        Point(0.88, 1.2096),
        Point(0.93, 1.3408),
        Point(0.99, 1.5236),
    ]
    x1 = [0.774]

    points2 = [
        Point(3.50, 33.1154),
        Point(3.55, 34.8133),
        Point(3.60, 36.5982),
        Point(3.65, 38.4747),
        Point(3.70, 40.4473),
        Point(3.75, 42.5211),
        Point(3.80, 44.7012),
        Point(3.85, 46.9931),
        Point(3.90, 49.4024),
        Point(3.95, 51.9354),
        Point(4.00, 54.5982),
        Point(4.05, 57.3975),
        Point(4.10, 60.3403),
        Point(4.15, 63.4340),
    ]
    x2 = [3.5516, 3.7505, 3.9004, 4.0507]

    Print(points1, x1, "Интерполяционная формула Лагранжа:", Lagrange)
    Print1(points2, x2, Newton1, Newton2)

Main()


# Класс для представления точки на плоскости
class Point:
    # Инициализация объекта класса Point
    def init(self, x, y):
        self.X = x  # Установка координаты X
        self.Y = y  # Установка координаты Y

# Функция для интерполяции методом Лагранжа
def Lagrange(points, x):
    lagrangePol = 0  # Инициализация значения полинома Лагранжа

    # Перебор всех точек
    for i in range(len(points)):
        basicsPol = 1  # Инициализация базисного полинома

        # Расчет базисного полинома
        for j in range(len(points)):
            if j != i:
                basicsPol *= (x - points[j].X) / (points[i].X - points[j].X)

        # Суммирование базисного полинома
        lagrangePol += basicsPol * points[i].Y

    return lagrangePol  # Возвращение значения полинома Лагранжа

# Функция для интерполяции методом Ньютона с разделенными разностями (формула 1)
def Newton1(points, x):
    n = len(points)  # Количество точек
    y = [[0]*n for _ in range(n)]  # Создание матрицы для хранения разделенных разностей

    # Заполнение первого столбца матрицы значениями Y
    for i in range(n):
        y[i][0] = points[i].Y

    # Расчет разделенных разностей
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

    # Вычисление значения интерполяционного многочлена
    sum = y[0][0]
    t = (x - points[0].X) / (points[1].X - points[0].X)
    chils = t
    znam = 1

    for i in range(1, n):
        znam *= i
        sum += (chils * y[0][i]) / znam
        chils *= (t - i)

    return sum  # Возвращение значения интерполяционного многочлена

# Функция для интерполяции методом Ньютона с разделенными разностями (формула 2)
def Newton2(points, x):
    n = len(points)  # Количество точек
    y = [[0]*n for _ in range(n)]  # Создание матрицы для хранения разделенных разностей

    # Заполнение первого столбца матрицы значениями Y
    for i in range(n):
        y[i][0] = points[i].Y

    # Расчет разделенных разностей
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            y[j][i] = y[j][i - 1] - y[j - 1][i - 1]

    # Вычисление значения интерполяционного многочлена
    sum = y[n - 1][0]
    t = (x - points[n - 1].X) / (points[1].X - points[0].X)
    chils = t
    znam = 1

    for i in range(1, n):
        znam *= i
        sum += (chils * y[n - 1][i]) / znam
        chils *= (t + i)

    return sum  # Возвращение значения интерполяционного многочлена

# Функция для вывода результатов интерполяции
def Print(points, x, title, interpolate):
    print("Исходные точки: ")
    for i in range(len(points)):
        print(f"{points[i].X:.3f}\t{points[i].Y:.5f}")

    print(f"\n{title}:")
    for i in range(len(x)):
        result = interpolate(points, x[i])
        print(f"{x[i]:.3f}\t{result:.5f}")

    print("------------------------------------")

# Функция для вывода результатов интерполяции с использованием двух формул Ньютона
def Print1(points, x, interpolate1, interpolate2):
    print("Исходные точки: ")
    for i in range(len(points)):
        print(f"{points[i].X:.3f}\t{points[i].Y:.5f}")

    for i in range(len(x)):
        if x[i] - points[0].X < points[-1].X - x[i]:
            result = interpolate1(points, x[i])
            title = 'Первая интерполяционная формула Ньютона:'
        else:
            result = interpolate2(points, x[i])
            title = 'Вторая интерполяционная формула Ньютона:'
        print(f"\n{title}")
        print(f"{x[i]:.3f}\t{result:.5f}")

    print("------------------------------------")

# Основная функция программы
def Main():
    points1 = [
        Point(0.68, 0.8086),
        Point(0.73, 0.8949),
        Point(0.80, 1.0296),
        Point(0.88, 1.2096),
        Point(0.93, 1.3408),
        Point(0.99, 1.5236),
    ]
    x1 = [0.774]

    points2 = [
        Point(3.50, 33.1154),
        Point(3.55, 34.8133),
        Point(3.60, 36.5982),
        Point(3.65, 38.4747),
        Point(3.70, 40.4473),
        Point(3.75, 42.5211),
        Point(3.80, 44.7012),
        Point(3.85, 46.9931),
        Point(3.90, 49.402)]