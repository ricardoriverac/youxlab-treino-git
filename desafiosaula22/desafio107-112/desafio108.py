import moedas

p = (float(input('Digite o preço: R$')))
print(f'A \033[35mmetade\033[m de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
print(f'O \033[34mdobro\033[m de R${moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'\33[36mAumentando 10%\033[m temos {moedas.moeda(moedas.aumentar(p, 10))}')
print(f'\033[32mDiminuindo 10%\033[m temos {moedas.moeda(moedas.diminuir(p, 10))}')
