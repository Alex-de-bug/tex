import null as null


def f(x):
    return (1 / 7) * x ** 7 - x ** 3 + (1 / 2) * x ** 2 - x


def quadratic_approximation(x1, x2, x3):
    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)
    numerator = 0.5 * ((x2 ** 2 - x3 ** 2) * f1 + (x3 ** 2 - x1 ** 2) * f2 + (x1 ** 2 - x2 ** 2) * f3)
    denominator = (x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3
    if denominator == 0:
        return null
    return numerator / denominator

def helper(x1, delta_x):
    x2 = x1 + delta_x
    f1 = f(x1)
    f2 = f(x2)
    if f1 > f2:
        x3 = x1+2*delta_x
    else:
        x3 = x1-delta_x
    f3 = f(x3)
    fmin = min(f1, f2, f3)
    if fmin == f(x1):
        xmin = x1
    elif fmin == f(x2):
        xmin = x2
    else:
        xmin = x3

    x_ = quadratic_approximation(x1, x2, x3)
    # print(f"x1: {x1} x2: {x2} x3: {x3} f1: {f1} f2: {f2} f3: {f3} xmin: {xmin} fmin:{fmin} x_:{x_} f(x_):{f(x_)}")
    if x_ == null:
        x1 = xmin
        return helper(x1)

    return x_, xmin, x1, x2

def checker(xmin, x_, epsilon):
    # print(x_)
    if abs((f(xmin) - f(x_)) / f(x_)) < epsilon and abs(
            (xmin - x_) / x_) < epsilon:
        return True
    return False

def stepper6(x1, x3, x2):
    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)
    fmin = min(f1, f2, f3)
    if fmin == f(x1):
        xmin = x1
    elif fmin == f(x2):
        xmin = x2
    else:
        xmin = x3

    x_ = quadratic_approximation(x1, x2, x3)
    # print(f"x1: {x1} x2: {x2} x3: {x3} f1: {f1} f2: {f2} f3: {f3} xmin: {xmin} fmin:{fmin} x_:{x_} f(x_):{f(x_)}")
    if x_ == null:
        x1 = xmin
        return x1, null

    return x_, xmin

def extremum_search(a, b, epsilon):
    delta_x = abs(a-b)/2
    x1 = a

    x_ = helper(x1, delta_x)[0]
    xmin = helper(x1, delta_x)[1]
    x1 = helper(x1, delta_x)[2]

    while True:
        if checker(x_, xmin, epsilon):
            return x_, f(x_)

        if (a<x_) and (b>x_):
            x_ = stepper6(a, b, x_)[0]
            xmin = stepper6(a, b, x_)[1]
            if xmin == null:
                x1 = x_
                x_ = helper(x1, delta_x)[0]
                xmin = helper(x1, delta_x)[1]
        else:
            x1 = x_
            x_ = helper(x1, delta_x)[0]
            xmin = helper(x1, delta_x)[1]



a = 1
b = 1.5
epsilon = 0.0001

# Выполнение алгоритма
extremum_x, extremum_value = extremum_search(a, b, epsilon)

print("Экстремум в точке x =", extremum_x)
print("Значение функции в этой точке f(x) =", extremum_value)
