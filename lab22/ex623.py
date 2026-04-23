import math

if __name__ == '__main__':
    A = [0, 0]
    B = [0, 1]
    C = [int(input("Введіть x 3-ої точки: ")), int(input("Введіть y 3-ої точки: "))]
    print(A, B, C)

    AB = round(math.sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1])), 2)
    AC = round(math.sqrt((C[0] - A[0]) ** 2 + (C[1] - A[1])), 2)
    BC = round(math.sqrt((C[0] - B[0]) ** 2 + (C[1] - B[1])), 2)

    angleA = round(math.degrees(math.acos((AB ** 2 + AC ** 2 - BC ** 2) / (2.0 * AB * AC))), 1)
    angleB = round(math.degrees(math.acos((AB ** 2 + BC ** 2 - AC ** 2) / (2.0 * AB * BC))), 1)
    angleC = round(math.degrees(math.acos((AC ** 2 + BC ** 2 - AB ** 2) / (2.0 * AC * BC))), 1)

    print("Кут А = ", angleA)
    print("Кут B = ", angleB)
    print("Кут C = ", angleC)

    for i in [angleA, angleB, angleC]:
        if i > 120:
            print("Точка з кутом {:f} є точкою Ферма".format(i))

    print([(j + k + l) / 3 for j, k, l in zip(A, B, C)])