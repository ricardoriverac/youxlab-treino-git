lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

# mostrando na tela de uma forma mais bonita
for comida in lanche:
    print(f'Eu vou comer {comida}')

#outra forma de mostrar e falar em qual posição esta o elemento
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#mostra a comida e em qual posição ela ta
for pos, comida in enumerate(lanche):
    print(f'EU vou comer {comida} na posição {pos}')

print(sorted(lanche)) #colocando a tupla em ordem

#juntando tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

#mostra quantas vezees aparece o elemento
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5))

#mostrar em qual posição ta o elemento (só conta o primeiro)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(2))

#deletando uma tupla
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)
print(pessoa)