frase = str(input('Digite uma frase: ')).upper()

frase2 = frase.replace(' ', '')

reverso = frase2[::-1]

o = reverso.replace(' ', '')

print(f'O inverso dessa frase é: {reverso}')

if frase2 == reverso:
    print('Essa frase é um palíndromo')
    
else:
    print('Essa frase não é um palíndromo')