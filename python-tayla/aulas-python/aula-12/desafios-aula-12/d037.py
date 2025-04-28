numero = int(input('Digite um número intiero: '))
print(""" escolha para ver o resultado da conversão
[1] binário
[2] octal
[3] hexadecimal""")

#variaveis de conversão 
binario = bin(numero)
octal = oct(numero)
hexa = hex(numero)

#msotrando o resultado
opcao = int(input('Qual é sua opção? '))
if opcao == 1:
    print(f'A conversão em binário é {binario}')
elif opcao == 2:
    print(f'A conversão em octal é {octal}')
else:
    print(f'A conversão em hexadecimal é {hexa}')