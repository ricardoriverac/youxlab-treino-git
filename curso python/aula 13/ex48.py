cont = 0
soma = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + 1
        cont = cont + c 
print ("A soma dos números pares são: {} de {} números digtados.".format(soma,cont))