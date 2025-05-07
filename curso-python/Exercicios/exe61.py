#Refaça o desafio 051, lendo o primeiro termo e a razao de uma PA, mostrando os 10
#primeiros termos da progressão usando a estrutura while.

primeiroTermo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
contador = 0

termo = primeiroTermo

print("Os 10 primeiros termos da PA são:")
while contador < 10:
    print(termo, end=" ")
    termo += razao
    contador += 1
print("fim")