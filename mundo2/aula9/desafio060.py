numero = int(input('Digite um número inteiro: '))
resultado = 1 
contador = 1 
while contador <= numero: 
    resultado *= contador
    contador += 1
print(f'O resultado de {numero}! é: {resultado}')