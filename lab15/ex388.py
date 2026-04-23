import random
import itertools as it

if __name__ == '__main__':
    a = [[random.randint(-10, 10) for _ in range(17)] for _ in range(17)]
    print(*a, sep='\n')
    maxValue = max(max(e for e in r) for r in a)
    print()
    print(*list(it.chain.from_iterable([[(i, j) for j in range(len(a)) if a[i][j] == maxValue] for i in range(len(a))])), sep='\n')