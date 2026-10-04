zak=input('Введите название заказа:')
name=input('Введите имя заказчика:')

namep1=input('Введите название позиции:')
kol1=int(input('Введите кол-во:'))
cost1=float(input('Введите стоимость 1:'))

namep2=input('Введите название позиции:')
kol2=int(input('Введите кол-во:'))
cost2=float(input('Введите стоимость 1:'))

dost=int(input('Введите стоимость доставки:'))
sum=int(input('Введите внесенную сумму:'))

st1=kol1*cost1
st2=kol2*cost2
stbezd=st1+st2
stsd=stbezd+dost
kol=kol1+kol2
sda=sum-stsd

print(50*'=')
print('Заказ:',zak)
print('Заказчик:',name)
print(50*'=')
print(f'{namep1} | {kol1} | {cost1:.2f} | {st1:.2f}')
print(f'{namep2} | {kol2} | {cost2:.2f} | {st2:.2f}')
print(50*'-')
print(f'Стоимость доставки:{dost:.2f}')
print(f'Стоимость без доставки:{stbezd:.2f}')
print(f'Стоимость с доставкой:{stsd:.2f}')
print(f'Кол-во товаров:',kol)
print(f'Внесено рублей:{sum:.2f}')
print(f'Сдача:{sda:.2f}')
