from time import sleep
total = totmil = menor = cont=0
barato=' '
print('-'*15)
print('BEM VINDO A NOSSA LOJA!!')
print('-'*15)
sleep(1)
print('Iniciando o site............')
print('-'* 15)
sleep(1)
while True:
    sleep(1)
    produto=str(input('Qual p nome do produto? '))
    preço=float(input('Qual o valor do produto?  '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont ==1:
        menor = preço
    else:
        if preço<menor:
            menor = preço
    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar ? [S/N]')).upper()
    if resp == 'N':
        break
print('Calculando...')
sleep(2)
print(f'O total de compra foi {total}')
print(f'A quantidade que custa mais de mil e {totmil}') 
print(f'O mais barato e {menor}')