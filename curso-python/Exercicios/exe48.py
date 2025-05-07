#Faça um programa que calcule a some entre todos os números impares que são multiplos
#de tres e que se encontram no intervalo de 1 ate 500
s = 0

for j in range(3, 501, 3):
    print(j, end=" ")
    s = s + j
print("\nA soma de todos os números ímpares múltiplos de 3 entre 1 e 500 é {}".format(s))