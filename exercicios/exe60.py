#Faça um programa que leia um número qualquer e mostre o fatorial.

#Ex: 5! = 5x4x3x2x1 = 120

numero = int(input("Digite um número: "))
contador = numero
fatorial = 1

while contador > 0:

    if contador == 1:
        print(f"{contador} = ", end="")
    else: 
        print(f"{contador} x ", end="")

    fatorial *= contador
    contador -= 1
print(fatorial)