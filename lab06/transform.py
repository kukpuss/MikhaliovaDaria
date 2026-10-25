text=input('Введите числа:')
n=list(map(int,text.split()))
m=n[:]
for i in range(len(m)):
    if m[i]<0:
        m[i]=abs(m[i])
print(f'Исходный список:{n}, новый список:{m}')