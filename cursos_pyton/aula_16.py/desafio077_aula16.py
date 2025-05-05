lista = 'amor', 'paz', 'felicidade', 'morango', 'chocolate', 'sol', 'paris', 'miami',
for palavra in lista:
    print(f'Na palavra {palavra.upper()} temos ' , end=' ')
    for letra in palavra:
        if letra in "aeiou":
            print(letra, end=' ')
    print('')