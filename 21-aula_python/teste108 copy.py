import  Desafio108copy 

preco = float(input('Digite o preço: R$ ' ))
print(f'A metade de {Desafio108copy.moeda(preco)} é {Desafio108copy.moeda(Desafio108copy.metade(preco))}')

print(f'O dobro de {Desafio108copy.moeda(preco)} é {Desafio108copy.moeda(Desafio108copy.dobro(preco))}')

print(f'Com o aumento de 10% fica {Desafio108copy.moeda(Desafio108copy.aumentar(preco,10))}')

print(f'')
