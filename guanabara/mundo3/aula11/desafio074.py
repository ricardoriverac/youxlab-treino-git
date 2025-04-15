from random import sample
listagem = tuple(sample(range(10), 5))
print(listagem)
print(f'O maior valor é {max(listagem)} e o menor é {min(listagem)}.')