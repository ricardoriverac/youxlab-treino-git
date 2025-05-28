import moeda
import dados
print('---'*15)
p = ''
p = dados.leiaDinheiro(f'Digite o preço - {moeda.moeda(p)}'.center(30))
moeda.resumo(p, 10/2, 16/2)