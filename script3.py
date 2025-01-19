import numpy as np

# Определяем функцию
def f(x):
    return np.sin(22 * x) + np.sqrt(x**2 + 22 * x)

# Метод трапеций
def trapezoidal_method(f, a, b, n):
    h = (b - a) / n  # Шаг разбиения
    integral = 0.5 * (f(a) + f(b))  # Учитываем граничные точки

    for i in range(1, n):
        x = a + i * h  # Точка разбиения
        integral += f(x)  # Добавляем значение функции в точке

    integral *= h  # Умножаем на шаг
    return integral

# Параметры
a = 22  # Начало отрезка
b = 44  # Конец отрезка
n = 1  # Начальное количество интервалов

# Вычисляем интеграл для n = 1, 5, ..., 5^10
for i in range(11):
    result = trapezoidal_method(f, a, b, n)
    result_str = f"{result:.12f}".replace(".", ",")  # Заменяем точку на запятую
    print(f"n = {n}: Значение интеграла = {result_str}")
    n *= 5  # Увеличиваем n в 5 раз