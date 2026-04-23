import random

if __name__ == '__main__':
    n = int(input("Введіть n: "))
    nums = [random.randint(-10, 10) for i in range(n)]
    print(nums)
    print(max(i + j for i, j in zip(nums[:n // 2 + 1], nums[n // 2 + 1::-1])))
    print(min(i * j for i, j in zip(nums[:n // 2 + 1], nums[n // 2 + 1:])))