a = 0

while True:
    c = int(input("Введите целое число: "))
    if c > 0:
        break
    a += 1

print(f"Квадрат: {c * c}")
print(f"Отклонено попыток: {a}")