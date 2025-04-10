numero = 0
contadorNumeros = 0 
soma = 0
while numero != 999:
    numero = int (input("Digite um número, ou digite \033[33m999\033[m para sair do programa: "))
    if  numero != 999:
        contadorNumeros += 1
        soma = numero + soma
print ("Você saiu do programa!!")
print ("Foram digitados  \033[36m{}\033[m  números. A soma entre eles é:  \033[36m{}\033[m ".format(contadorNumeros,soma))
