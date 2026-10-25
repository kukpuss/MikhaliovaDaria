text=input('Введите числа:')
n=list(map(int, text.split()))
if not n:
    print('Нет данных')
else:
    print(f'Кол-во:{len(n)}, сумма:{sum(n)}, минимум:{min(n)}, максимум:{max(n)}, среднее:{(sum(n)/len(n)):.2f}')