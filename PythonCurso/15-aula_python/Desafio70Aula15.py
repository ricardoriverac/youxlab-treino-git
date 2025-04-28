total = produtos1000 = menor = contador = 0

print('='*112)
print('                                  LOJA DO CRUZEIRO ')
print('='*112)

while True:
    nome = str(input('Qual o nome do seu produto? '))
    preco = float(input('Qual o valor do seu produto? '))
    contador +=1
    
    total += preco
    if preco > 1000:
        produtos1000 =+1
        

    if contador == 1:
        menor = preco
        barato = nome

    else:
        if preco < menor:
            menor = preco
            barato = nome 

    
    responda = ' '
    while responda not in 'SN':
        responda =str(input('Você quer continuar cadastrando produtos? [S/N]')). upper() .strip()
        

    if responda == 'N':
        break

print(f'O total da sua compra foi R${total:.2f}')
print(f'{produtos1000}, Produtos ultrapassou R$1000')
print(f'O Produto mais barato foi {barato} que custou R${menor:.2f} ')
    