import math
from itertools import takewhile

if __name__ == '__main__':
    nums = [7, 6, 5, 8, 2, 3, -2, -5, 3, -5, -8]
    print(nums)
    print(math.prod(n for n in takewhile(lambda num: num >= 0, nums)))
