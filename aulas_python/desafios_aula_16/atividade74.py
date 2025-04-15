import random
escolhapc = (random.choices([1,4,2,7,4,2,8,9,10], k=5))
maximo = max(escolhapc)
minimo = min(escolhapc)

print(f'Números aleatorios gerador: {escolhapc}\nO maior número é: {maximo}\nO menor número é {minimo}')