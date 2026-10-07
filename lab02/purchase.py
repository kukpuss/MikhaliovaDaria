price = int(input("Цена одной тетради (целые рубли): "))
count = int(input("Количество тетрадей: "))
paid = int(input("Переданная сумма (рубли): "))

cost = price * count
change = paid - cost

print(f'Стоимость: {cost}')
print(f'Сдача: {change}')