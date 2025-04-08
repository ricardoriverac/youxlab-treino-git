import random
n = ()
for c in range(5):
    num = random.randint(0,1000)
    n += (num, )

print(f'Os números sorteados foram: {n}')
print(f'O maior número sorteado foi {max(n)}')
print(f'O menor número sorteado  {min(n)}')