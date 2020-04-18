a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
z = input("Ведите знак")
if z == "+":
    summ=a+b
    print(str(a)+str(z)+str(b)+" = " + str(summ))
if z == "-":
    summ=a-b
    print(str(a)+str(z)+str(b)+" = "+str(summ))
if z == "*":
    summ=a*b
    print(str(a)+str(z)+str(b)+" = "+str(summ))
if z =="/":
    summ=a/b
    print(str(a)+str(z)+str(b)+" = "+str(summ))