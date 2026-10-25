text=input('Введите числа:')
n=list(map(int,text.split()))
m=[]
if not n:
    print('Нет данных')
else:
    maxim=max(n)
    for ind,c in enumerate(n):
        if c==maxim:
            m.append(ind)
    print(m)