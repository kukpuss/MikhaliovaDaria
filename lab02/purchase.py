price = int(input("Цена одной тетради: "))
count = int(input("Количество тетрадей: "))
paid = int(input("Переданная сумма: "))

cost = price * count
change = paid - cost

print(f'Стоимость: {cost}')
print(f'Сдача: {change}')
