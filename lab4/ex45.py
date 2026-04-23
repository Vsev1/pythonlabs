def printnums(a, b, c, d):
    print("a = ", str(a), ", b = ", str(b),
          ", c = ", str(c), ", d = ", str(d))

if __name__ == '__main__':
    a = float(input("Введіть а: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть с: "))
    d = float(input("Введіть d: "))

    if a <= b <= c <= d:
       a = b = c = d = max(a, b, c, d)
       printnums(a, b, c, d)
    elif a > b > c > d:
        printnums(a, b, c, d)
    else:
        printnums(a ** 2, b ** 2, c ** 2, d ** 2)