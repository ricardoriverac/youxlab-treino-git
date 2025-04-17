lanche=('hamburguer', 'suco', 'pizza', 'pudim' )
print( lanche[2])



lanche=('hamburguer', 'suco', 'pizza', 'pudim' )
print( lanche[1:3])
lanche=('hamburguer', 'suco', 'pizza', 'pudim' )
for comida in lanche:
    print(f'Eu quero comer {comida}')
   print('comi muito')

lanche=('hamburguer', 'suco', 'pizza', 'pudim', 'refrigerante' )
print(len(lanche))
print('comi muito')
 
    
lanche=('hamburguer', 'suco', 'pizza', 'pudim', 'refrigerante' )
del lanche
for cont in range(0,len (lanche)):
   print(f'eu vou comer {lanche[cont]}')

lanche=('hamburguer', 'suco', 'pizza', 'pudim', 'refrigerante' )
for cont in range(0,len (lanche)):
    print(f'eu vou comer {lanche[cont]} na posiçao {cont}')


for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} e na posiçao {pos}')
    
    
