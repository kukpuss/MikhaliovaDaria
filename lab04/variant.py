n = int(input("Введите n: "))

c = 0
sum = 0

for i in range(n):
    a = int(input(f"Введите число {i + 1}: "))
    if a % 2 == 0:
        c += 1
        sum += a

print(f"Количество: {c}")
print(f"Сумма: {sum}")