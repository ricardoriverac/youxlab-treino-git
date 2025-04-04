#Crie um programa onde o usuario possa digitar sete valores números e cadastre-os
#Em uma lista unica que mantenha separados os valores pares e impares. No final, mostre
#os valores pares e impares em ordem crescente.

valores = [[], []]

for n in range(7):
    num = int(input("Digit um número: "))

    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
        
print(f"\nSua lista completa: {valores}")
print(f"A lista de números pares são: {sorted(valores[0])}")
print(f"A lista de números impares são: {sorted(valores[1])}")