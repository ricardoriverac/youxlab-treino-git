from utilidadesCev import moedas
from utilidadesCev import dados

preco = dados.leiaDinheiro('Digite um número: ') 
taxa = dados.leiaDinheiro('Digite a taxa: ')
moedas.resumo(preco,taxa,True)
