from utilidadesCeV import moedas
from utilidadesCeV import dados

preco = dados.leiaDinheiro('Digite o preço: R$')
moedas.resumo(preco, 32, 21)