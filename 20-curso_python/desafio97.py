def escrever(frase):
    print('~' *len(frase))
    print(frase)
    print('~' *len(frase))
    print( )

dicionario = dict()


for frases in range (1, 4):
        frase = str(input(f'{frases} - Escreva algo: ')).upper()
        dicionario[f'frase{frases}'] = frase
    
for k in dicionario:
      escrever(dicionario[k])