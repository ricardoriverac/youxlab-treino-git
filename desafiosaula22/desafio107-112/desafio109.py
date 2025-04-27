import moedas

p = (float(input('Digite o preço: R$')))
print(f'A \033[35mmetade\033[m de {moedas.moeda(p)} é {moedas.metade(p, True)}')
print(f'O \033[34mdobro\033[m de R${moedas.moeda(p)} é {moedas.dobro(p, True)}')
print(f'\33[36mAumentando 10%\033[m temos {moedas.aumentar(p, 10, True)}')
print(f'\033[32mDiminuindo 10%\033[m temos {moedas.diminuir(p, 10, True)}')
