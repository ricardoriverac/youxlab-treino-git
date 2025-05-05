preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 6 / 100)
print(' O produto que custava R${}, na promoção com desconto de 6% vai custar R$ {}'.format(preco, novo))