import random

print('Estou pensando em um número aleatório de 1 a 5 \n e gostaria que você tentasse acertar qual é')
n = int(input('Qual número estou pensando?: '))
c = random.randint(1, 5)
print(f'O número que eu pensei foi {c}')
if n == c:
    print('PARABÉNS! Acertou em cheio!')
else:
    print('Não foi dessa vez :(, mas não desista!')
