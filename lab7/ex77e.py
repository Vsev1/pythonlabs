from math import cos, sin, prod

if __name__ == '__main__':
    n = int(input("Введіть n: "))

    print(prod(sum(cos(i) for i in range(1, n + 1)) / sum(sin(i) for i in range(1, n + 1)) for i in range(1, n + 1)))
