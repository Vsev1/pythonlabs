if __name__ == '__main__':
    n = int(input("Введіть n: "))
    print([2 ** i + 3 ** (i + 1) for i in range(1, n + 1)])
