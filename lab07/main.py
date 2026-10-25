from functions import s, a, n, select_numbers

num = int(input('Введите целое число:'))
print(f'Сумма цифр: {s(num)}')

num = list(map(int, input('Введите числа:').split()))
avg = a(num)
if avg is None:
    print('Нет данных')
else:
    print(f'Среднее: {avg:.2f}')

text = input('Введите текст:')
print(f'Нормализованный текст: {n(text)}')

t = int(input('Введите порог:'))
print(f'Выборка: {select_numbers(num, t)}')