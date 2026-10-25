text=input('Введите числа:')
n=list(map(int,text.split()))
m=[]
for i in n:
    if i%2==0:
        m.append(i)
msort=sorted(m)
print(m,f'Кол-во:{len(m)}, сумма:{sum(m)}, отсортированная копия:{msort}')