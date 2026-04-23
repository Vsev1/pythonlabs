from math import cos, prod

if __name__ == '__main__':
    n = int(input("Введіть n: "))
    x = float(input("Введіть x: "))

    print(prod(k / (k + 1) - cos(abs(x)) ** k for k in range(1, n + 1)))

