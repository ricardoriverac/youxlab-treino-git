frase = str(input('Digite uma frase: ')).upper()
fraseSemEspaco = frase.replace(' ', '')
reverso = fraseSemEspaco[::-1]
juntar = reverso.replace(' ', '')
print(f'O inverso dessa frase é: {reverso}')
if fraseSemEspaco == reverso:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')