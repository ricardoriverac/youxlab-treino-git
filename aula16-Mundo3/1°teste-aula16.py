lanche= ('hambúrguer', 'suco', 'pizza', 'pudim') #TUPLAS  são sempre entre PARENTESES 
#              0         1        2        3
print(lanche) #mostra todas as comidas da variável
print(lanche[1]) #mostra somente a comida 1, no caso o suco 
print(lanche[3])

print(lanche[-2]) #mostra a pizza
print(lanche[-1]) #mostra o pudim

print(lanche[1:3]) #mosta as comidas entre esses n°, no caso, suco e pizza 

print(lanche[2:]) #mostra da comida 2 até o final, no caso, pizza e pudim
print(lanche[-3:]) #mostra da comida 3 contando de trás para frente até o final
print(lanche[:2]) #mostra do início até  a comida 2 PORÉM ele ignora o ponto 

#                        TUPLAS SÃO IMUTÁVEIS

for comida in lanche:
    print(f'Eu vou comer comida {comida}')
print('Comi muito!')
print('OUTRA FORMA')    
for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posição {contador}') #aqui mostras as posições dos elementos 
print('Comi muito!')
print('OUTRA FORMA')    
for posicao, comida in enumerate(lanche): # para cada comida escreva
    print(f'Eu comi {comida} na posição {posicao}')
print('Comi muito!')

print('EM ORDEM') # NÃO altera a tupla
print(sorted(lanche))



