if __name__ == '__main__':
    # 1
    s = input("Введіть строку: ").split()
    print("Кількість слів: ", len(s))

    # 2
    print("Кількість букв 'а' в останьому слові: ", s[len(s) - 1].count("а"))

    # 3
    print("Кількість слів, що починаються з літери 'б': ",
          len([i for i in s if i.startswith("б")]))

    # 4
    print("Кількість слів, у яких перший і останній символи однакові: ",
          len([i[0] == i[-1] for i in s]))

    # 5
    print("Слово, яке починається з літери 'а': ", [w for w in s if w[0] == 'а'][0])

    # 6
    print(" ".join(s).replace("это", "то"))

    # 7
    print(min(s, key=len))




