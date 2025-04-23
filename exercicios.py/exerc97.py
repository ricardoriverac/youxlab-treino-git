def escrever(frase):
    print('~' * len(frase))
    print(frase)
    print('~' * len(frase)) 
    print( )

lista = {}

for frases in range(1, 4):
    frase = str(input(f'{frases} - Digite algo: ')).upper
    lista[f'frase{frase}'] = frase

for k in lista:
    escrever(lista[k])