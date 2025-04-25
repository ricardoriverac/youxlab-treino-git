from ex107 import moeda

pergunta = float(input('Digite um preço: R$'))

moeda.linha()
print(f'A metade de {pergunta} é {moeda.metade(pergunta)}')
print(f'O dobro de {pergunta} é {moeda.dobro(pergunta)}')
print(f'Aumentando 30% temos {moeda.aumentar(pergunta, 30)}')
print(f'Reduzindo 20% temos {moeda.diminuir(pergunta, 20)}')