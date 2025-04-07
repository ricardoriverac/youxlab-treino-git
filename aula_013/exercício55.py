lst =[ ] 
for c in range(1, 6):

    peso=float(input('Peso da {}ª pessoa: '.format(c)))

    lst+=[peso]

print('O Maior peso foi:', max(lst))

print('O Menor peso foi:', min(lst))