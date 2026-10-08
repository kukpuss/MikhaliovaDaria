t= int(input("Общий объём: "))
c = int(input("Вместимость единицы: "))

f = t // c
o = t % c
v = (t + c - 1) // c

print(f"Полных единиц: {f}")
print(f"Остаток: {o}")
print(f"Всего единиц: {v}")