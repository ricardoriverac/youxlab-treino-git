produto=float(input('Digite um valor:'))
desconto= 5/100*produto 
preço=(produto - desconto)
print('Analizando o valor{},seu desconto é {}, e o valor {}'.format(produto, desconto,preço))