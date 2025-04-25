import random
menor = 99999999
maior = 0
lista = []
for i in range(1, 5):
    choice = random.randint(1, 10)
    print (f'{choice} ', end= '')
    if choice > maior:
        maior = choice
    if choice < menor:
        menor = choice
lista = choice
print(lista)
print(f'O maior número é o {maior}')
print(f'O menor número é o {menor}')