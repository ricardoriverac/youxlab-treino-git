preco = float(input('Qual o valor do seu produto?'))
r = (preco *5) /100
s = preco - r

print('você teve um desconto de: R${:<.2f} e o preço ficou em R${} '.format(r, s))
