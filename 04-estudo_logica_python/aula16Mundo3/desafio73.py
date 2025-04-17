times=('Flamengo','Palmeiras','Fluminense','Ceará','Bragantino','Vasco','Juventude','Mirassol', 'Internacional',
'Botafogo','Fortaleza','Santos','Corinthians','chapecoense','Cruzeiro','São Paulo','Grêmio','Bahia','Atlético-MG', 'Sport')
print(f' Cinco primeiros colocados {times[0:5]}' )
print(f' os ultimos quatro colocados são:{times[-4:]}')
print(f' os times em ordem alfabetica{sorted(times)}')
print(f'O time chapecoense esta na posiçao {times.index("chapecoense")+1}')