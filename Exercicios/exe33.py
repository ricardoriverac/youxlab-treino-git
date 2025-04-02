#Faça um programa que leia tres números e mostre qual é o maior e qual e o menor

n1 = int(input("Qual é o 1° número? "))
n2 = int(input("Qual é o 2° número? "))
n3 = int(input("Qual é o 3° número? "))

menor = min(n1, n2, n3)

maior = max(n1, n2, n3)

print(f"O menor valor é {menor}")
print(f"O maior valor é {maior}")
