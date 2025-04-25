import  Desafio109 

preco = float(input('Digite o preço: R$ ' ))
print(f'A metade de {Desafio109.moeda(preco)} é {(Desafio109.metade(preco, True))}')
print(f'O dobro de {Desafio109.moeda(preco)} é {(Desafio109.dobro(preco,True))}')
print(f'Com o aumento de 10% fica {(Desafio109.aumentar(preco,10,True))}')


