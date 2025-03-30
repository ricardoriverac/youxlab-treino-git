frase = str(input('Digite a frase: ')).strip().upper()
separar = frase.split()
juntar = ''.join(separar)
inverso = '' 
for letra in range(len(juntar)-1 , -1 , -1):
    inverso += juntar[letra]
print(f'A frase {juntar} no inverso é {inverso}')
if inverso == juntar:
    print('A frase é um palíndromo') 
else:
    print('A frase digitada não é um palíndromo')