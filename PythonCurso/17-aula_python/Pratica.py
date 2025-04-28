valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor')))

    
for c, v in enumerate(valores):
    print(f' Na posção {c} achei o valor {v}...', end=' ')
print('Cheguei no final da lista')