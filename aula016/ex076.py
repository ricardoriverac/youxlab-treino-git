lista=('Lápis ',1.75,'Caneta ',2.50,'Muchila ',110,' Borracha ',1.50, ' Bolsinha ',5.00
            ,'Caderno',15,'Apontador ',2)

for produtos in range(len(lista)):

    if produtos % 2==0:
        print(f'{lista[produtos]:.<20} ',end='')
#[] são usados para acessar elementos de uma tupla ou lista
#produtos =index

    else:
        print(f'{lista[produtos]} ')



print(f'{lista[0]}')