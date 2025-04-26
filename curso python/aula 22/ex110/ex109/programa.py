import moeda
print('\n' + '\033[35m-\033[m'*40)
preco = float(input('Digite o preço: R$ '))
moeda.resumo(preco, 20, 12)
