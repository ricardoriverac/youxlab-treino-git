import random
lista = []

print('--'*35)
print('JOGO DA MEGA-SENA'.center(70))
print('--'*35)
jogos = int(input('Quantos jogos você quer fazer? '))
print(f'=== SORTEANDO {jogos} JOGOS... ===')
for c in range(jogos):
  
    jogo = sorted(random.sample(range(1, 61), 6))
    lista.append(jogo)
    print(f'Jogo {c+1}: {jogo}')
print('--'*35)
print('BOA SORTE NA SUA TENTATIVA!')
