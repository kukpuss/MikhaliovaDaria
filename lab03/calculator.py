a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
p = input("Введите операцию (+, -, *, /): ")

if p == "+":
    result = a + b
    print(f"{result:.2f}")
elif p == "-":
    result = a - b
    print(f"{result:.2f}")
elif p == "*":
    result = a * b
    print(f"{result:.2f}")
elif p == "/":
    if b == 0:
        print("Деление на ноль запрещено")
    else:
        result = a / b
        print(f"{result:.2f}")
else:
    print("Неизвестная операция")