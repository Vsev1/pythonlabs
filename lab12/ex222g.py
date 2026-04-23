import random
from math import sqrt

if __name__ == '__main__':
    n = int(input("Введіть n: "))
    nums = [random.randint(-10, 10) for i in range(n)]
    print(nums)
    print(sum((sqrt(i) - i) ** 2 if 0 < i <= 15 else 2.7 for i in nums))

