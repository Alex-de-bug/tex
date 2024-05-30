import numpy as np
from scipy.optimize import minimize_scalar

# Определение функции и ее градиента
def f(x):
    x1, x2 = x
    return -x1 - 4*x2**2 + 2*x1*x2 + x1

def grad_f(x):
    x1, x2 = x
    return np.array([2*x2, 2*x1 - 8*x2])

# Метод наискорейшего спуска
def steepest_descent_method(f, grad_f, x0, max_iterations=1000):
    k = 1
    x = x0
    history = [x]  # Сохраняем историю шагов

    while k < max_iterations:
        gradient = grad_f(x)
        grad_norm = np.linalg.norm(gradient)

        # Шаг 1. Проверка условия остановки
        if grad_norm < epsilon:
            break  # Достигнут критерий остановки

        # Вычисление направления спуска
        s = -gradient / grad_norm

        # Шаг 2. Решение задачи одномерной оптимизации
        phi = lambda alpha: f(x + alpha * s)  # Одномерная функция для оптимизации
        res = minimize_scalar(phi)  # Минимизация phi
        alpha_k = res.x  # Оптимальный размер шага

        # Обновление x
        x = x + alpha_k * s
        history.append(x)

        # Шаг 3. Переход к следующей итерации
        k += 1

    return x, history

# Начальное приближение
x0 = np.array([1, 2])

# Параметры метода
epsilon = 1  # Погрешность

# Выполнение метода наискорейшего спуска
x_min, history = steepest_descent_method(f, grad_f, x0, epsilon)

print(f"Минимум достигается в точке: {x_min}")
print(f"Значение функции в минимуме: {f(x_min)}")
print(f"Количество итераций: {len(history)}")
