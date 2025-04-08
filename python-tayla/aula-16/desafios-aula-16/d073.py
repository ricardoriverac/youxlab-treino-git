times = ('Internacional', 'Corinthians', 'Ceará SC', 'Fortaleza', 'Botafogo', 'Flamengo', 'Palmeiras', 'Juventude', 'Fluminense', 'Grêmio', 'Vasco da Gama', 'Cruzeiro', 'Bahia', 'São Paulo', 'Bragantino', 'Santos', 'Mirassol', 'Sport Recife', 'Atlético-MG', 'EC Vitória')
posicao = 'Mirassol'

print('\033[1;33m-=\033[m' * 20)
print(f'\033[1mLista de times do brasileirão:\033[m{times}')

print('\033[1;33m-=\033[m' * 20)
print(f'\033[1mEsses são os 5 primeiros colocados:\033[m{times[0:5]}')

print('\033[1;33m-=\033[m' * 20)
print(f'\033[1mEsses são os 4 últimos colocados:\033[m {times[-4:]}')

print('\033[1;33m-=\033[m' * 20)
print(f'\033[1mTimes em ordem alfabética:\033[m', sorted(times))

print('\033[1;33m-=\033[m' * 20)
print(f'\033[1mO Mirassol está na {times.index(posicao)}ª posição\033[m')