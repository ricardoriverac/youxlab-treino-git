numero=[2,3,4,9,5,1]
numero[2]=3
numero.append(7)
numero.sort(reverse=True)
numero.remove(2)
print(numero)
print(f'essa lista tem {len(numero)}')


valores=[]
valores.append(9)
valores.append(7)
valores.append(5)
for v in valores:
    print(f'{v}...',end=' ')