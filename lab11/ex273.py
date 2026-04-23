import random
from math import sqrt

if __name__ == '__main__':
    n = int(input("Введіть n: "))
    x = [random.randint(0, 10) for i in range(n)]
    y = [random.randint(0, 10) for j in range(n)]
    z = [random.randint(0, 10) for k in range(n)]
    p = [random.randint(1, 10) for f in range(n)]

    for i, j, k, m in zip(x, y, z, p):
        print("Точка({:d}, {:d}, {:d}) з масою = {:d}.".format(i, j, k, m))

    xc = sum(a * b for a, b in zip(x, p)) / sum(p)
    yc = sum(a * b for a, b in zip(y, p)) / sum(p)
    zc = sum(a * b for a, b in zip(z, p)) / sum(p)

    print('Xc = {:.3f} \nYc = {:.3f} \nZc = {:.3f}'.format(xc, yc, zc))
    print("Відстані від центру тяжіння до точок:")
    print(['{:.3f}'.format(sqrt((a - xc) ** 2 + (b - yc) ** 2 + (c - zc) ** 2)) for a, b, c in zip(x, y, z)])
