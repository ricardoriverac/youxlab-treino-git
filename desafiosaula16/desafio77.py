palavras = ('LER', 'PYTHON', 'PROGRAMACAO', 'LIVROS',
            'DEUS', 'CACHORRINHO', 'BARBIE', 'FANTASIA',
            'DESING', 'CURSO', 'GUANABARA', 'FRONTEND')
for p in palavras:
    print(f'\nNa palavras {p} temos ', end = '')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print('\033[35m', letra, '\033[m', end=' ')
print('')
            