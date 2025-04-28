from ex108 import moeda

pergunta = float(input('Digite o preço: R$'))

moeda.linha()
print(f'A metade de {moeda.moeda(pergunta)} é {moeda.moeda(moeda.metade(pergunta))}')
print(f'O dobro de {moeda.moeda(pergunta)} é {moeda.moeda(moeda.dobro(pergunta))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(pergunta, 10))}')