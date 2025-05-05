soma = 0 
for numero in range(1, 501): 
    if numero % 2 != 0: 
        if numero % 3 == 0: 
            soma += numero 
print("A soma dos múltiplos é: {}.".format(soma))