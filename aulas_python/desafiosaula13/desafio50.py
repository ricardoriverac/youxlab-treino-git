soma = 0
contador = 0
for c in range (1, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma+=n
        contador+= 1
print('Você informou {} números pares e a soma desses valores é {}'.format(contador, soma))
