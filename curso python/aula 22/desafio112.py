from utilidadesCeV import dado
from utilidadesCeV import moeda

preco = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(preco, 30, 12)
