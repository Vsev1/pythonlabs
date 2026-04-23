if __name__ == '__main__':
    n = int(input("Введіть n: "))
    # x = int(input("Введіть x: "))
    a = [[j + i if j + i <= n else 2 * n - i - j for j in range(1, n + 1)] for i in range(n)]

    print(*a, sep='\n')