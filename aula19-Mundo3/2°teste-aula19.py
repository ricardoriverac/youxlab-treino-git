dados={'nome':'Ana Beatriz', 'sexo':'F', 'idade':17}

print('CHAVES:')
for chave in dados.keys():  #para cada chave no dicionário 
    print(chave)  #mostra as chaves (ex: nome ou idade)

print()

print('VALORES:')
for valor in dados.values():   #para cada valor no dicionário 
    print(valor)  #mostra os valores (ex: Ana Beatriz ou 17)

print()

print('ITENS:')
for chave, valor in dados.items():   #para item chave e o item valor no dicionário  
    print(f'{chave} = { valor}')  #mostra os itens (mostra todo conteúdo do dicionário)