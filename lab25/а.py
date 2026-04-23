if __name__ == '__main__':
    a = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    b = list(reversed(a[1:])) + a  # vertical mirror
    c = list(zip(*b))  # transpose
    print(*c, sep='\n')
    d = list(reversed(c[1:])) + c  # another vertical mirror
    print()
    e = list(zip(*d))  # transpose again
    print()
    print(*e, sep='\n')