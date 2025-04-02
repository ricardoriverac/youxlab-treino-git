maiorpeso = 0
menorpeso = 0


for pess in range(1, 6):
    peso=float(input('Peso da pessoa {}? '.format(pess)))
    if pess == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso

        if peso < menorpeso:
            menorpeso = peso
print('O maior peso lido foi de {}Kg'.format(maiorpeso))
print('O menor peso lido foi de {}Kg'.format(menorpeso))