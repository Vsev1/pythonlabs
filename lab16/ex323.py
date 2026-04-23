import math

if __name__ == '__main__':
    try:
        n = int(input("Введіть число: "))
        if n < 1:
                raise ValueError
        print([i for i in reversed(range(1, n)) if math.gcd(i, n) == 1])
    except ValueError:
        print("Неправильно введені дані")
        exit(1)