import numpy as np

def f(x):
    x1, x2 = x
    # return 2*x1+4*x2-x1**2 - 2*x2**2
    return -x1 - 4*x2**2 + 2*x1*x2 + x1

def grad_f(x):
    x1, x2 = x
    # return np.array([2 - 2*x1, 4 - 4*x2])
    return np.array([2*x2, 2*x1 - 8*x2])

# Метод градиентного спуска
def gradient_descent(f, grad_f, x0, alpha, epsilon):
    max_iterations = 3
    x = x0
    history = [x]

    for i in range(max_iterations):
        x_prev = x
        print(f'Значение функции при начальном приближении: {f(x_prev)}')
        print(f'Градиент в этой точке: ({grad_f(x_prev)[0]}, {grad_f(x_prev)[1]})')
        x1 = x[0] + alpha * (grad_f(x)[0])
        x2 = x[1] + alpha * (grad_f(x)[1])
        x = np.array([x1, x2])
        history.append(x)

        print(f'oldx1:{x_prev[0]} oldx2:{x_prev[1]} new x1: {x1} new x2: {x2} f(X): {f(x_prev)} f(new X): {f(x)} abs: {abs(f(x) - f(x_prev))}')
        if (abs(f(x) - f(x_prev)) < epsilon) or (len(history) > max_iterations):
            return x, history
    return x, history

x0 = np.array([1, 2])
alpha = 0.25
epsilon = 0.05
x_min, history = gradient_descent(f, grad_f, x0, alpha, epsilon)

print(f"Минимум достигается в точке: {x_min}")
print(f"Значение функции в минимуме: {f(x_min)}")
print(f"Количество итераций: {len(history)}")
