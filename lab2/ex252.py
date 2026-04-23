if __name__ == '__main__':
    # 1
    s = input("Введіть строку: ")
    print("Число символів '+': ", s.count("+"),
          "\nЧисло символів '*': ", s.count("*"))

    # 2
    print("Загальне число символів '+', '—', '*' в строці: ",
          len([i for i in s if i in '+-*']))  # s.count('+') + s.count('-') + s.count('*')
