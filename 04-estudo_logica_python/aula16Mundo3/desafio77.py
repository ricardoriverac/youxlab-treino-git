lista = 'linda', 'princesa',' fabulosa','paz','morango', 'bala'\
    'musica', 'professora', 'amor'
for palavra in lista:
    print(f' Na palavra {palavra.upper()} temos ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
