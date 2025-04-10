termo1 = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
dec = (termo1 + (10-1)*razao)
counter = termo1
while counter<= dec:
    print('{}'.format(counter))
    counter += razao