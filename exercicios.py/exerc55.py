lista = []

for peso in range (1, 6):
    kg = float(input('Digite o peso da {} pessoa: '.format(peso)))
    lista.append (kg)
menor = min(lista)
maior = max(lista)
print ('O maior peso é {}'.format(maior))
print ('O menor peso é {}'.format(menor))
