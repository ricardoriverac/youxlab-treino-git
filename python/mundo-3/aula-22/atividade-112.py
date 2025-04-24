from utilidadesCeV import moeda
from utilidadesCeV import dado

valor = float(dado.leiaDinheiro('Digite um valor: '))
taxa_cambio = float(input('Digite a taxa de câmbio do dólar: '))
moeda.resumo(valor, taxa_cambio)
