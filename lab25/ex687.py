# import math
#
# import numpy as np

if __name__ == '__main__':
    n = int(input("n = "))
    a = [[j + i if j + i <= n else 0 for j in range(1, n + 1)] for i in range(n)]
    print(*a, sep="\n")
