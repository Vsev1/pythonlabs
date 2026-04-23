import math

if __name__ == '__main__':
    print("Введіть довжини сторін AB, BC та AC: ")
    AB = float(input("AB = "))
    BC = float(input("BC = "))
    AC = float(input("AC = "))

    A = math.degrees(math.acos((AB ** 2 + AC ** 2 - BC ** 2) / (2.0 * AB * AC)))
    B = math.degrees(math.acos((AB ** 2 + BC ** 2 - AC ** 2) / (2.0 * AB * BC)))
    C = math.degrees(math.acos((AC ** 2 + BC ** 2 - AB ** 2) / (2.0 * AC * BC)))

    print("Кут А = ", round(A, 1))
    print("Кут B = ", round(B, 1))
    print("Кут C = ", round(C, 1))





