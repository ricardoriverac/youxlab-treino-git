#SOMANDO SOMENTE OS PARES
soma=0
cont=0
for contador in range(1,7):
    numero=int(input('Digite o {}° número:'.format(contador)))
    if numero % 2 == 0:
        soma+=numero
        cont+=1
print(f'Você adicionou {cont} números PARES , a soma deles é igual:{soma}')
