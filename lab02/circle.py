import math

radius = float(input('Введите радиус (> 0): '))

c = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f'Длина окружности: {c:.2f}')
print(f'Площадь круга: {area:.2f}')