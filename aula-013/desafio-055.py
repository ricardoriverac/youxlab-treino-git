maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('O peso da {} pessoa:'.format(p)))
    if p == 1: #vai definir o maior e o menor de cara por que foi unico lido até o momento do laço
        maior = p #vai receber valor do primeiro peso que a pessoa digitou e vai definir como o maior
        menor = p #vai receber o valor do primeiro peso que a pessoa digitou e vai  definir como menor
    #if peso <= maior: #se o peso que pessoa digitou for menor doq o numero maior que definimos anteriormente 

    else:
        if peso > maior: #se o peso for maior que o maior peso que ja tem, o maior vira vai virar o peso que vai vir na sequencia 
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}kg'.format(maior))
print('O menor peso foi de {}kg'.format(menor))

#maior = 9999999
#menor = 0
#for g in range(1, 6):
    #pso = float(input('Digite o peso da {} pessoa'.format(g)))
    #if pso < maior:
        #menor = pso
    #if pso > maior:
        #maior = pso
#print('O maior peso foi de {}'.format(maior))
#print('o menor peso foi {}'.format(menor))


