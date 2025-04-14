lanche = ('sanduiche', 'sorvete', 'chocolate', 'coxinha')
print(lanche[1])
print(lanche[-1])
print (lanche[1:3])

for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('OLOCO TÔ CHEIO')

for cont in range(0, len(lanche)):
    print(f'Eu comi {lanche[cont]} na posição {cont}')
print('AI COMI MUITO TA MALUCO')

for pos, comida in enumerate(lanche):
   print(f'Eu comi {comida} na posição {pos}')
   
print(sorted(lanche))

a = (1, 7, 9)
b = (8, 2, 5, 1)
c = a + b
print(c)
print(c.index(1, 8))