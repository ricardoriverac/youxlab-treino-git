#Escreva um programa que leia um numero inteiro qualquer e peça para o usuario
#escolher qual será a base de conversão:

#1 para binario
#2 para ocatal
#3 para hexadecimal

numero = int(input("Digite um número: "))
escolha = input("Qual voce deseja: 1 - Binario, 2 - Ocatal, 3 - Hexadecimal: ").lower

if escolha in ["binário" or "binario"] or 1:
    binario = bin(numero)[2:]
    print(f"O número {numero} em binário é: {binario}")

elif escolha == "ocatal" or 2:
    octal = format(numero, 'o')
    print(f"O número {numero} em octal é: {octal}")

elif escolha == "hexadecimal" or 3:
    hexadecimal = format(numero, 'x')
    print(f"O número {numero} em hexadecimal é: {hexadecimal}")
    
else: print("Erro")
