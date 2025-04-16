lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são imútaveis
print(lanche)
print(sorted(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')

# for cont in range(0, len(lanche)):
#     print (f'Eu vou comer {lanche [cont]} na posição {cont}')
    
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))

