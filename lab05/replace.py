text=input('Введите текст:')
c=0
for i in text:
    if i==':':
        c+=1
a=text.replace(':','-')
print(c,f'Новая строка:{a}')