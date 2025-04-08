from random import randint
lista = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
organizado = (sorted(lista))
print(f'→ Os números gerados foram: {lista}.')
print(f'→ O menor número foi {organizado[0]}.')
print(f'→ O menor número foi {organizado[4]}.')
