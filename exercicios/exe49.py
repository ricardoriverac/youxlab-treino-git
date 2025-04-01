#Refaça o desafio 009, mostrado a tabuada de um número que o usuario escolher
#so que agora ultilizando o laço for

num = int(input("Digite um número inteiro: "))

print(f"\nTabuada do {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
