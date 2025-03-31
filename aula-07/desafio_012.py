preço = float(input('Qual é o preço do produto? R$'))
porcentagem = preço * 0.05
total = preço - porcentagem
print('O produto que custava R${},na promoçao com desconto de 55% vai custar R${}'.format(preço, total))