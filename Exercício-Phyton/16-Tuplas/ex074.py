from random import randint

numeros = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

print(f'Os valores sorteados foram: ', end='' )

for n in numeros:
    print(f'{n} ', end='')  

print(f'\n O maio número sorteado foi {max(numeros)}')

print(f'O menor número sorteado foi {min(numeros)}')