import random


def swap(matrix, col1, col2):
    """
    Swaps the specified columns of the matrix
    """
    for e in matrix:
        e[col1], e[col2] = e[col2], e[col1]


if __name__ == '__main__':
    try:
        a = [[random.randint(-10, 10) for _ in range(24)] for _ in range(18)]
        print(*a, sep="\n")
        print("\n")
        i = int(input("Введіть i-й стовпець: "))
        j = int(input("Введіть j-й стовпець: "))
        if not (0 <= i <= 23 and 0 <= j <= 23 and i < j):
            raise ValueError
        swap(a, i, j)
        print(*a, sep="\n")
    except ValueError:
        print("Неправильно введені дані")
        exit(1)