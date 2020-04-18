a = int(input('Введите первое число:'))
z = str(input('Ар знак:(+,-,/,*)'))
b = int(input('Ведите второе число:'))
if z =='+':
    r = a+b
    print(r)
elif r =='-':
    r = a-b
    print(r)
elif r =='/':
    r = a/b
    print(int(r))
elif r == '*':
    r = a*b
    print(r)
else:
    print('Неправельно введён знак')