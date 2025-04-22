#ESTATÍSTICAS DE PRODUTOS
contador=menor=cont1000=total=0
barato=''
while True:
    print('LOJA TUDO BARATO')
    nome=str(input('Nome do produto: ')).strip()
    valor=float(input('Valor do produto: R$ '))
    total+=valor
    contador+=1
    if valor>=1000:
        cont1000+=1
    if contador==1 or valor < menor:
        menor=valor
        barato=nome
    escolha= ' '
    while escolha not in 'SN':
        escolha=str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha=='N':
        break
print(f'O total é de R${total:.2f}')
print(f'{cont1000} produtos a cima de R$1000.00')
print(f'O produto mais barato foi {barato} custou R${menor:.2f}')