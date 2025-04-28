from random import sample
numeros = tuple(sample(range(10), 5))
print(numeros)
print(f'o maior valor é {max(numeros)} e o menor é {min(numeros)}.')