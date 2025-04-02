#Faça um programa que mostre a tabuada de varios numeros, um de cada vez
#para cada valor digitado pelo usuario. O programa sera interrompido
#quando o número solicitado foi negativo.

while True:
    n = int(input("Digite um número: "))

    if n < 0:
        break

    for j in range(1, 11):
        m = j * n
        print(n, "X", j, "=", m)
print("Tabuada encerrada.")