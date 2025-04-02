#Faça um programa que leia o peso de cinco pessoas. No final
#Mostre qual foi o maior e o menor peso lidos

maiorPeso = 0
menorPeso = float('inf')

for i in range(5):
    peso = float(input(f"Digite o peso da {i+1}ª pessoa: "))
    
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso

print("\nO maior peso foi: {} kg".format(maiorPeso))
print("O menor peso foi: {} kg".format(menorPeso))