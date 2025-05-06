soma= 0
contador= 0
for a in range(1, 7):
    numero= int(input('Digite o {}° valor: '.format(a)))
    if numero % 2 == 0: 
        soma += numero 
        contador += 1
print('Você informou {} números PARES e a soma foi {}'.format(contador, soma))
