### Варіант № 31
### Завдання № 694 б
# Отримати квадратну матрицю порядку $n$:
# $\left[\begin{array}{cc}
# ... & 0 & 0 & 0 & 1\\
# ... & 0 & 0 & 2 & 0\\
# ... & 0 & 3 & 0 & 0\\
# . & . & . & . & .\\
# n & 0 & 0 & 0 & ...
# \end{array}\right]$


if __name__ == '__main__':
    n = int(input("Введіть n: "))
    a = [[0 if j == i else j + i for j in range(n)] for i in range(n)]
    print(*a, sep="\n")

