from moeda2 import * 

preco = float(input('Digite o preço: R$'))
form = str(input('Deseja mostrar os números formatados? ')).lower()[0]


print(f'Aumentando 10% de {format(preco,form)} temos {format(aumentar(preco),form)}')
print(f'Diminuindo 15% de {format(preco,form)} temos {format(diminuir(preco),form)}')
print(f'O dobro de {format(preco,form)} é {format(dobro(preco),form)}')
print(f'A metade de {format(preco,form)} é {format(metade(preco),form)}')