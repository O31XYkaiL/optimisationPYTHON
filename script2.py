import numpy as np

# Определяем функцию
def f(x):
    return np.sin(22 * x) + np.sqrt(x**2 + 22 * x)

# Метод центральных прямоугольников
def central_rectangles_method(f, a, b, n):
    h = (b - a) / n  # Шаг разбиения
    integral = 0  # Инициализация интеграла

    for i in range(n):
        x_mid = a + (i + 0.5) * h  # Середина интервала
        integral += f(x_mid)  # Добавляем значение функции в середине интервала

    integral *= h  # Умножаем на шаг
    return integral

# Параметры
a = 22  # Начало отрезка
b = 44  # Конец отрезка
n = 1  # Начальное количество интервалов

# Вычисляем интеграл для n = 1, 5, ..., 5^10
for i in range(11):
    result = central_rectangles_method(f, a, b, n)
    result_str = str(result).replace(".", ",")
    print(f"n = {n}: Значение интеграла = {result_str}")
    n *= 5  # Увеличиваем n в 5 раз