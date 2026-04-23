import math

if __name__ == '__main__':
    a = float(input("Введіть а: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть с: "))

    # ax^2 + bx + c = 0
    discr = b ** 2 - 4 * a * c
    print("Дискримінант = ", str(discr))

    if discr > 0:
        print("Корені:\nx1 = ", str((-b + math.sqrt(discr)) / 2 * a),
              "\nx2 = ", str((-b - math.sqrt(discr)) / 2 * a))
    elif discr == 0:
        print("Корені:\nx1 = ", str(-b / 2 * a), "\nx2 = ", str(-b / 2 * a))
    else:
        print("Коренів немає")