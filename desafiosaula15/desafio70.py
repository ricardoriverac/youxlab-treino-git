print('-='*20)
print('\033[1;35mLOJA DA IZINHA\033[m')
print('-='*20)
totalGasto = produtosMaisDeMil = soma = menorpreco = 0
produtoMaisBarato = ''
menorP = float('inf')
while True:
    produto = input('O que você deseja comprar?: ')
    preco = float(input('Qual é o preço?: '))
    maisProdutos = input('Deseja comprar mais produtos?[S/N]: ').upper()
    soma+=preco
    
    if preco < menorP:
        menorP = preco
        produtoMaisBarato = produto
               
    if preco>1000:
        produtosMaisDeMil+=1
        
    if maisProdutos=='N':
        print('Affs, pobre! Volte sempre! ')
        break
    
print(f'O \033[35mTOTAL GASTO\033[m na compra foi {soma}')
print (f'Você comprou {produtosMaisDeMil} \033[36mPRODUTOS\033[m que são \033[36mMAIS DE R$1000\033[m')
print(f'O \033[33mPRODUTO\033[m mais \033[33mBARATO\033[m é o {produtoMaisBarato} que custa {menorP} ')

        