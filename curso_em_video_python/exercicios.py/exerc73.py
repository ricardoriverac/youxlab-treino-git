times = ['CAMPEONATO 2025', 'Flamengo', 'Palmeiras', 'Juventude', 'Vasco', 'Fluminense', 'Internacional', 'Fortaleza', 'Ceará SC', 'Corinthians', 'Botafogo', 'Bragantino', 'Cruzeiro', 'Grêmio', 'Bahia', 'São Paulo', 'Mirassol', 'Atlético-MG', 'Santos', 'EC Vitória', 'Sport Recife']
timesPraOrdem = ['Flamengo', 'Palmeiras', 'Juventude', 'Vasco', 'Fluminense', 'Internacional', 'Fortaleza', 'Ceará SC', 'Corinthians', 'Botafogo', 'Bragantino', 'Cruzeiro', 'Grêmio', 'Bahia', 'São Paulo', 'Mirassol', 'Atlético-MG', 'Santos', 'EC Vitória', 'Sport Recife']
enfeite = ('-' *20 )
enfeite = ('-' *20 )

print(f'{enfeite} \033[1;35m5 PRIMEIROS COLOCADOS\033[m {enfeite}')
for colocados in range(1, 6):
    print(f'{colocados}° {times[colocados]}')
    
print(f'{enfeite}\033[1;35mÚLTIMOS 4 COLOCADOS\033[m {enfeite}')
for ultimos in range(17, 21):
    print(f'{ultimos}° {times[ultimos]}')

print(f'{enfeite}\033[1;35mTIMES EM ORDEM ALFABÉTICA\033[m {enfeite}')
for alfabetico in range (0, 20):
    ordemAlfabetica = sorted(timesPraOrdem)
    print(f'  {ordemAlfabetica[alfabetico]}')

print(f'{enfeite}\033[1;35mEM QUE POSIÇÃO ESTÁ O TIME CRUZEIRO\033[m {enfeite}')
posicao = times.index('Cruzeiro') 
print(f'O time Cruzeiro está na posição {posicao}')
