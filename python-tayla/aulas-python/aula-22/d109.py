from ex109 import moeda

pergunta = float(input('Digite o preço: R$'))

moeda.linha()
print(f'A metade de {moeda.moeda(pergunta)} é {moeda.metade(pergunta, True)}')
print(f'O dobro de {moeda.moeda(pergunta)} é {moeda.dobro(pergunta, True)}')
print(f'Aumentando o valor em 10% temos {moeda.aumentar(pergunta, 10, True)}')
print(f'Reduzindo o valor em 13% temos {moeda.diminuir(pergunta, 13, True)}') 