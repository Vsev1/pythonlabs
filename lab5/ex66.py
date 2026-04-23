if __name__ == '__main__':
    k = float(input("Введіть k: "))
    m = float(input("Введіть m: "))
    x = float(input("Введіть x: "))
    y = float(input("Введіть y: "))
    z = float(input("Введіть z: "))

    if k < m ** 2:
        print("x = ", str(abs(x)), ", y = ", str(y - 0.5), ", z = ", str(z - 0.5))
    elif k == m ** 2:
        print("x = " + str(x - 0.5) + ", y = " + str(abs(y)) + ", z = " + str(z - 0.5))
    else:
        print("x = " + str(x - 0.5) + ", y = " + str(y - 0.5) + ", z = " + str(abs(z)))
