a = int(input("Введите число от 0 до 100: "))

if a < 0 or a > 100:
    print("Ошибка диапазона")
elif a <= 19:
    print("Низкий")
elif a <= 79:
    print("Средний")
else:
    print("Высокий")