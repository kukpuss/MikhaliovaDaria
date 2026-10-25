text=input('Введите текст:')
a=text.split()
m=[]
for i in a:
    s=i.strip('.,!?;:').lower()
    if s=='':
        continue
    if s.startswith('а'):
        m.append(s)
if not m:
    print('Нет совпадений, кол-во:0')
else:
    for i in m:
        print(i)
    print(f'Кол-во:{len(m)}')
