import  ds109

preco = float(input('Digite o preço: R$ ' ))
print(f'A metade de {ds109.moeda(preco)} é {(ds109.metade(preco, True))}')
print(f'O dobro de {ds109.moeda(preco)} é {(ds109.dobro(preco,True))}')
print(f'Com o aumento de 10% fica {(ds109.aumentar(preco,10,True))}')