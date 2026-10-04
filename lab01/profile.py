lastn=input('Введите вашу фамилию:')
name=input('Введите ваше имя:')
group=input('Введите вашу группу:')
city=input('Введите ваш город:')
year=int(input('Введите ваш возраст:'))
favsub=input('Введите ваш любимый предмет:')
hoursweek=float(input('Введите количество часов подготовки в неделю:'))

year=year+4
hoursweek4=hoursweek*4
srhours=hoursweek/7

print(f'Ваши фамилия и имя:{'lastn'+' '+'name'}')
print('Через 4 года вам будет:',year)
print('Ваше время подготовки за 4 недели:',hoursweek4)
print(f'Ваше среднее время подготовки в день: {srhours:.2f}')

