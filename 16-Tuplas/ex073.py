print('========== Tabela Do Brasileirão 2025 ==========')
cont = 0
pos = 0
times = ('Flamengo', 'Palmeiras', 'Fluminense', 'Ceará SC'
         'Bragantino', 'Vasco da Gama', 'Juventude', 'Mirassol',
         'Internacional', 'Botafogo', 'Fortaleza', 'Santos', 'Corinthians'
         'EC Vitória', 'Cruzeiro', 'São Paulo', 'Gremio', 'Bahia', 
         'Atletico-MG', 'Spor Refice')

print('=================================================')

for cont in range (1, len(times)):
    print(f' {times[cont]} na posição {cont}') 

print('=================================================')

print(f'Os 5 primeiros times da tabela são:{times[0:6]}')

print('==================================================')

print(f'Os 4 ultimos times da tabela são:{times[-4:]}')

print('===================================================')

print(f'O time do Cruzeiro está na posição {12}')