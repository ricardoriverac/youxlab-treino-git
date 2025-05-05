#MENOR E MAIOR PESO DE PESSOAS
maior=0
menor=0
for peso in range(1,6):
    peso1=float(input(f'Digite o peso da {peso}° pessoa:'))
    if peso==1:
        maior=peso1
        menor=peso1
    else:
        if peso>maior:
            maior=peso1
        if peso<menor:
            menor=peso1
print('O MAIOR peso foi de {}kg'.format(maior))
print('O MENOR peso foi de {}kg'.format(menor))
