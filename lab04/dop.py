n = int(input("Введите n >= 2: "))

if n < 2:
    print("Ошибка: n должно быть >= 2")
else:
    p = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            p = 0
            break
        d += 1

    if p:
        print("Простое")
    else:
        print("Составное")