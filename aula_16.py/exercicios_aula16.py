#lanche =('Hambúrguer", "Suco', 'Pizza', 'Pudim') 
#print(lanche [1:3])








lanche =('Hambúrguer", "Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba !')



lanche =('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'batata frita')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba !')



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