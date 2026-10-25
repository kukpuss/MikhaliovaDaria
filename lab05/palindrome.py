text=input('Введите текст:')
a=text.lower().replace(' ','')
if a=='':
    print('Нет текста')
else:
    if a[::-1]==a:
        print('Палиндром')
    else:
        print('Не палиндром')