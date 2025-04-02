#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
#desconsiderando os espaços

#exemplo: ovo, otto

frase = input("Digite uma frase: ").replace(" ", "").lower()

if frase == frase[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")
