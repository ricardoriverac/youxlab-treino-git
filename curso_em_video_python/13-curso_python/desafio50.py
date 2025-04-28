soma = 0
conta = 0

for numeros in range(1,7):
    num= int(input('Escolha o {}° valor: '.format(numeros)))
    if num % 2 == 0 :
        soma += num
        conta += 1
print('A soma dos {} números pares é {}'.format(conta, soma))