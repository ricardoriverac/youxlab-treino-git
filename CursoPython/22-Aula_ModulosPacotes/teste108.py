import  ds108

preco = float(input('Digite o preço: R$ ' ))
print(f'A metade de {ds108.moeda(preco)} é {ds108.moeda(ds108.metade(preco))}')

print(f'O dobro de {ds108.moeda(preco)} é {ds108.moeda(ds108.dobro(preco))}')

print(f'Com o aumento de 10% fica {ds108.moeda(ds108.aumentar(preco,10))}')

print(f'')