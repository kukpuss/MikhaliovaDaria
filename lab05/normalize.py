text=input('Введите текст:')
n=" ".join(text.split())
print(n,f'Слов:{len(n.split())}')
print(f'Исходная длина:{len(text)},новая длина:{len(n)}',)