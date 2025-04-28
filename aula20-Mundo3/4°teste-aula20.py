def soma(*valores):
    soma=0
    for numero in valores:
        soma+=numero
    print(f'Somando os valores {valores} temos {soma}')
soma(2,1)
soma(3,2,2)

