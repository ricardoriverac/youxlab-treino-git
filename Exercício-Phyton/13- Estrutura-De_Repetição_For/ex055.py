pessoa  = float(input('Peso da 1ª pessoa: '))
pessoa2 = float(input('Peso da 2ª pessoa: '))
pessoa3 = float(input('Peso da 3ª pessoa: '))
pessoa4 = float(input('Peso da 4ª pessoa: '))
pessoa5 = float(input('Peso da 5ª pessoa: '))

lista = {pessoa, pessoa2, pessoa3, pessoa4, pessoa5} 


max1 = max(lista)
min2 = min(lista)

print('O maior peso lido foi de {}kg'.format(max1))
    

print('O menor peso lido foi de {}kg'.format(min2))
    