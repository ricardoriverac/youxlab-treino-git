from time import sleep
print('-='*20)
print('\033[1;35mLOJA DA IZINHA\033[m')
print('-='*20)
sleep(2)

totalGasto = produtosMaisDeMil = soma = menorpreco = 0
produtoMaisBarato = ''
menorP = float('inf')

while True:
    produto = input('O que você deseja comprar?: ')
    sleep(1)
    preco = float(input('Qual é o preço?: '))
    sleep(1)
    maisProdutos = input('Deseja comprar mais produtos?\033[33m[S/N]:\033[m ').upper()
    sleep(1)
    soma+=preco
    
    if preco < menorP:
        sleep(1)
        menorP = preco
        produtoMaisBarato = produto
               
    if preco>1000:
        sleep(1)
        produtosMaisDeMil+=1
        
    if maisProdutos != 'N' and maisProdutos !='S':
        sleep(1)
        print('\033[31mErro na digitação!\033[m Tente novamente ')
        maisProdutos = input('Deseja comprar mais produtos?\033[33m[S/N]:\033[m ').upper()
        if maisProdutos=='N':
            break
        
    if maisProdutos=='N':
        sleep(1)
        print('Affs, pobre! Volte sempre! ')
        break
    
print(f'O \033[35mTOTAL GASTO\033[m na compra foi R${soma}')
print (f'Você comprou {produtosMaisDeMil} \033[36mPRODUTOS\033[m que são \033[36mMAIS DE R$1000\033[m')
print(f'O \033[33mPRODUTO\033[m mais \033[33mBARATO\033[m é o {produtoMaisBarato} que custa R${menorP} ')

        