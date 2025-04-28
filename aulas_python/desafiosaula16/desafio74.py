import random
numeros = random.sample(range(1, 11), 5)
numerosAleatórios = tuple(numeros)
maior = max(numerosAleatórios)
menor = min(numerosAleatórios)
print('Os números sorteados foram: ')
print(numerosAleatórios)
print(f'O \033[35mMAIOR\033[m número sorteado é {maior}')
print(f'O \033[35mMENOR\033[m  número sorteado é {menor}')

