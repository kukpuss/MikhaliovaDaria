n = int(input("Введите n: "))

sum = 0
p = 0
max= 0

for i in range(n):
    a = int(input(f"Введите число {i + 1}: "))
    sum += a
    if a > 0:
        p += 1
    if a > max:
        max = a

print(f"Сумма: {sum}")
print(f"Положительных: {p}")
print(f"Максимум: {max}")