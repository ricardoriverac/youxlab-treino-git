
from random import choice , randint
maior = 0
menor = 0
computador = ((randint(0,10) , randint(0,10) , randint(0,10) , randint(0,10) , randint(0,10) ))
print(choice(computador) , choice(computador) , choice(computador) , choice(computador) , choice(computador))

# #print(sorted(computador))

print(f'O menor foi o {min(computador)} ')
print(f'O maior foi o {max(computador)} ')