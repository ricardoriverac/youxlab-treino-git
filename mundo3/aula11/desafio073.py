tabela = (
    'Internacional', 'Corinthians', 'Ceará', 'Fortaleza', 'Botafogo',
    'Flamengo', 'Palmeiras', 'Juventude', 'Fluminense', 'Grêmio',
    'Vasco da Gama', 'Cruzeiro', 'Bahia', 'São Paulo', 'Atlético-MG',
    'Santos', 'Sport Recife', 'Mirassol', 'Atlético-GO', 'Vitória'
)

print(20 * '=-')
print('OS 5 PRIMEIROS COLOCADOS DA SÉRIE A 2025')
for pos, time in enumerate(tabela[:5], start=1):
    print(f'O time {time} está na {pos}° posição na tabela')

print(20 * '=-')
print('OS 4 ÚLTIMOS COLOCADOS DA SÉRIE A 2025')
for pos, time in enumerate(tabela[-4:], start=17):
    print(f'O time {time} está na {pos}° posição na tabela')

print(20 * '=-')
print('A ordem alfabética dos times:')
print(sorted(tabela))

print(20 * '=-')
print(f'O Corinthians está na {tabela.index("Corinthians") + 1}° posição')
