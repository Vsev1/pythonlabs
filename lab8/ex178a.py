import random

if __name__ == '__main__':
    n = int(input("Введіть n: "))
    nums = [random.randint(1,10) for i in range(n)]
    print(nums)
    print(sum(i % 2 == 1 for i in nums))
