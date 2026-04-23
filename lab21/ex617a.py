import random
from math import sqrt

if __name__ == '__main__':
    n = int(input("Введіть n: "))
    counter = [c for c in range(1, n + 1)]
    x = [random.randint(-10, 10) for i in range(n)]
    y = [random.randint(-10, 10) for j in range(n)]
    r = [random.randint(1, 10) for k in range(n)]

    for c, i, j, k in zip(counter, x, y, r):
        print("Коло {:d}: центр в ({:d}, {:d}), радіус = {:d}.".format(c, i, j, k))

    s = 0
    for i in range(n):
        for j in range(i + 1, n):
            if sqrt((x[j] - x[i]) ** 2 + (y[j] - y[i]) ** 2) <= (r[j] + r[i]):
                print("Кола {:d} и {:d} перетинаються".format(i + 1, j + 1))
                counter += 1
            else:
                print("Кола {:d} и {:d} не перетинаються".format(i + 1, j + 1))

    print('Є' if s >= 3 else 'Немає')