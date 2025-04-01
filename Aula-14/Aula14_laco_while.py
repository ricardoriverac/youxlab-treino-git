#Laço de repetição

'''for j in range(1,10):
    print("Olá", j)
print("Fim")'''

'''contador = 1

while contador < 10:
    print(contador)
    contador += 1
print("Fim")'''

'''for j in range(1, 5):
    numero = int(input("Digite um número: "))
print("Fim")'''

'''numero = 1'''

#!= 0: ponto de parada

'''while numero != 0:
    numero = int(input("Digite um número: "))
print("Fim")'''

'''resposta = "S"

while resposta == "S":
    numero = input("Digite um valor: ")
    resposta = input("Quer continuar: [S/N]").upper()
print("Fim")'''

numero = 1
par = impar = 0

while numero != 0:
    numero = int(input("Digite um número: "))
    if numero != 0:
        if numero % 2 == 0:
            par += 1
        else: impar += 1
print(f"Voce digitou {par} números pares e {impar} números impares.")