preco = float(input('Digite o preço do seu produto'))
desconto = preco - (preco * 5 / 100)
print('O produto custava R${} e com a promoção de 5% vai custar {}'.format (preco,desconto))