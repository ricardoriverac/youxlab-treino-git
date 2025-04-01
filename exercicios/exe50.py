#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
#daqueles que forem pares. se o valor digitado foi impar, desconsidere-o.

soma = 0

for j in range(1, 6):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        soma += numero
print("A soma dos números é {}".format(soma))