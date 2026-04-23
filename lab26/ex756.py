import math
import itertools

if __name__ == '__main__':
    x = float(input("Введіть x: "))
    e = float(input("Введіть e: "))
    a = int(input("Введіть a: "))
    print(1 + sum(math.prod(a - k for k in range(k + 1)) / math.factorial(k) * x ** k for k in itertools.takewhile(
        lambda i: abs(math.prod(a - i for i in range(i + 1)) / math.factorial(i) * x ** i) >= e, itertools.count(0))))
