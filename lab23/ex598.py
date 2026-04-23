import collections
import itertools
import random


def sign(num1, num2, num3):
    """
    Takes 3 values and determines the sign of each value in order.
    Returns 3 characters with datatype tuple
    """
    return tuple('-' if e < 0 else '+' for e in [num1, num2, num3])

if __name__ == '__main__':
    com = list(itertools.product('+-', repeat=3))
    print(com)
    n = int(input("Введіть n: "))
    nums = [random.randint(-10, 10) for _ in range(n)]
    print(nums)
    lst = [com.index(sign(i, j, k)) for i, j, k in zip(nums, nums[1:], nums[2:])]
    print(lst)
    print(collections.Counter(lst))