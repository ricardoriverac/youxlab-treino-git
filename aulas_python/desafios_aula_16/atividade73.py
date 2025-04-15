times  = 'Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Vitória', 'Atlético Mineiro', 'Fluminense', 'Grêmio', 'Juventude', 'Red Bull Bragantino', 'Santos', 'Mirassol', 'Sport', 'Ceará'

print(f'\nLista de times do brasilerão: {times}\n\033[1;31m','=-='*50,'\033[m')
print(f'Os 5 primeiros são {times[0:5]}\n\033[1;31m','=-='*50,'\033[m')
print(f'Os 4 ultimos são {times[-4:]}\n\033[1;31m','=-='*50,'\033[m')
print(f'Times em ordem alfabética: {sorted(times)}\n\033[1;31m','=-='*50,'\033[m')
print(f'O cruzeiro está em {times.index("Cruzeiro")} posição ')