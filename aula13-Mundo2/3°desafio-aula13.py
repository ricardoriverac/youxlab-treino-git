#SOMA DOS N° ÍMPARES MULTIPLOS POR 3 DE 1 À 500
soma=0
for numeros in range(1, 501, 2):
    if numeros%3==0:
        soma=soma+numeros
print(f'A soma é de :{soma}')