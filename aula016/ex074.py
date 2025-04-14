from random import randint

valores = ()

for c in range (0,5):
    sorteados = randint(0,10)
    valores += (sorteados,)
    print(valores)


print(f'O maior numero e {max(valores)}')
print(f'O menor numero e {min(valores)}')





    


