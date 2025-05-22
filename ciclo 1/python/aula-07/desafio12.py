preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5/ 100)
print('O valor de antes custava R${}, na promoção com 5% de desconto, deve custar R${}'.format(preço, novo))