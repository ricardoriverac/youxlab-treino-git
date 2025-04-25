# Refaça o desafio 09 e, mostrando a tabuada de um numero que o usuario escolher, 
# so que agora utilzando o laço for

# Solicita o numero da tabuada
#numero = int(input("Digite um número para ver sua tabuada: "))

#print(f"\nTabuada do {numero}:\n")

# Laço for para gerar a tabuada de 1 a 10
#for i in range(1, 11):
    #resultado = numero * i
    #print(f"{numero} x {i} = {resultado}")

numero = int(input('Digite o numero para ver sua tabuada'))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")




