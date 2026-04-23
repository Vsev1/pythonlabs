import math

def f(c, d, x1, x2):
    result = abs((math.sin(abs(c * (x1 ** 3) + d * (x2 ** 2) - c * d))) ** 3
                 / math.sqrt((c * (x1 ** 3) + d * (x2 ** 2) - x1) ** 2 + 3.14)) \
             + math.tan(c * (x1 ** 3) + d * (x2 ** 2) - x1)
    print("Результат =",round(result, 3))


if __name__ == '__main__':
    print("Введіть значення змінних c та d: ")
    c = float(input("c = "))
    d = float(input("d = "))

    # x^2 - 3x - |cd| = 0
    discr = (-3) ** 2 - 4 * 1 * -(abs(c*d))
    print("Дискримінант =", discr)

    if discr > 0:
        x1 =  (3 + math.sqrt(discr)) / (2 * 1)
        x2 = (3 - math.sqrt(discr)) / (2 * 1)
        print("x1 =", x1,  "\nx2 =", x2)
        f(c, d, x1, x2)
    elif discr == 0:
        x1 = 3 / (2 * 1)
        x2 = 3 / (2 * 1)
        print("x1 =", x1,  "\nx2 =", x2)
        f(c, d, x1, x2)
    else:
        print("Коренів немає")