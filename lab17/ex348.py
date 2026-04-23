import collections
import random

if __name__ == '__main__':
    n = int(input("Введіть n: "))
    nums = [random.randint(-10, 10) for _ in range(n)]
    nums2 = [random.randint(-10, 10) for _ in range(n)]
    # nums = [1, 2, 3, 4, 5]
    # nums2 = [3, 5, 2, 1, 4, 3]
    print(nums, nums2)
    print("Не відрізняються" if collections.Counter(nums) == collections.Counter(nums2) else "Відрізняються")
