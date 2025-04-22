from utilidadesCeV import moeda
from utilidadesCeV import dado

num = float(dado.leiaDinheiro('Digite um preço: R$ '))
moeda.resumo(num, 80, 50)
