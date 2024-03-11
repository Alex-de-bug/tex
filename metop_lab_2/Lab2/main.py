def f(x):
    return 1/7*(x**7)-x**3+1/2*(x**2)-x

def d(x):
    return x**6-3*(x**2)+x-1

def d2(x):
    return 6*(x**5)-6*x+1

def method_of_dividing_a_segment_in_half(a, b, epsilon):
    print("Результат метода половинного деления")
    # print("Номер итерации a b x1 x2 f(x1) f(x2) b-a")
    left = a
    right = b
    iteratoins = 0
    while True:
        iteratoins+=1;
        x1 = (left + right - epsilon) / 2
        x2 = (left + right + epsilon) / 2
        y1 = f(x1)
        y2 = f(x2)
        if y1 > y2:
            left = x1
        else:
            right = x2
        # print(iteratoins, left, right, x1, x2, y1, y2, right - left)
        if right - left < 2 * epsilon:
            print("Ответ: x = "+str(((left + right) / 2))+"; y = "+ str(f((left + right) / 2))+"\n")
            return (left + right) / 2

def method_of_chords(a, b, epsilon):
    print("Результат метода хорд")
    left = a
    right = b
    inter = 0
    while True:
        inter+=1
        x = left - d(left) / (d(left) - d(right)) * (left - right)
        dx = d(x)
        # print(f"Iter: {inter};a: {left:.3f}; b: {right}; f'(a): {d(left):.3f}; f'(b): {d(right):.3f}; x: {x:.3f}; |f'(x)|: {abs(dx):.3f}")

        if abs(dx) <= epsilon:
            print("Ответ: x = "+str(x)+"; y = "+ str(f(x))+"\n")
            return

        if dx > 0:
            right = x
        else:
            left = x

def method_of_newtons(epsilon, x0):
    print("Результат метода касательных")
    x = x0
    itera = 0
    while True:
        itera+=1
        # print(f"Итерация: {itera}; x: {x:.3f}; f'(x): {d(x):.3f}; f''(x): {d2(x):.3f}; new x: {x - d(x) / d2(x):.3f}; |f'(x)| = {abs(d(x))}")
        if abs(d(x)) <= epsilon:
            print("Ответ: x = "+str(x)+"; y = "+ str(f(x))+"\n")
            return x
        x = x - d(x) / d2(x)

def method_of_golden(a, b, epsilon):
    print("Результат метода золотого сечения")
    x1 = a+0.382*(b-a)
    x2 = a + 0.618*(b - a)
    f1 = f(x1)
    f2 = f(x2)
    # print(f"Первая итерация: x1 = {x1:.3f}; x2 = {x2:.3f}; f(x1) = {f1:.3f}; f(x2) = {f2:.3f}")

    # Main loop
    iteration = 1
    while abs(b - a) > epsilon:
        # print(
        #     f"Iteration {iteration}: a = {a}, b = {b}, x1 = {x1}, x2 = {x2}, f(x1) = {f1}, f(x2) = {f2}, |b-a| = {abs(b - a)}")
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + 0.328 * (x2 - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + 0.618 * (b - x1)
            f2 = f(x2)

        iteration += 1
        # if(abs(b - a) < epsilon):
            # print(
            #     f"Iteration {iteration}: a = {a}, b = {b}, x1 = {x1}, x2 = {x2}, f(x1) = {f1}, f(x2) = {f2}, |b-a| = {abs(b - a)}")

    print(f"Ответ: x = {(a + b) / 2}; y ={f((a + b) / 2)}\n")
    return (a + b) / 2



a, b = 1, 1.5
epsilon = 0.05

method_of_dividing_a_segment_in_half(a, b, epsilon)
method_of_golden(a, b, epsilon)
method_of_chords(a, b, epsilon)
method_of_newtons(epsilon, 1.2)