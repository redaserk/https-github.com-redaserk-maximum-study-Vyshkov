try:
    var_1 = int(input("Введите значение переменной 1: "))
    var_2 = int(input("Введите значение переменной 2: "))
except ValueError:
    print("Вы ввелм недопустимое значение")
else:
    print(var_1 + var_2)