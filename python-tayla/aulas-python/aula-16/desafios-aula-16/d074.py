from random import randint

tupla = ()

for c in range(5):
    computador = randint(0,10)
    tupla = tupla + (computador, )
    
print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')