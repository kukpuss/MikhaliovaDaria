t = int(input("Введите общее количество секунд (>= 0): "))

hours = t // 3600
r = t % 3600
minutes = r // 60
seconds = r % 60

print(f'{hours} ч {minutes} мин {seconds} с')