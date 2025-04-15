# troquei a chapecoense pelo mirassol, porque a chapecoense está na serie b do campeonato.
times = ('Cruzeiro', 'flamengo','são paulo',
'palmeiras','botafogo','fortaleza,',
'fluminense','vasco','ceará',
'sport','juventude','bragantino',
'grêmio','bahia','vitória',
'internacional','patético-mg','santos',
'mirassol')

print('<->' * 15)
print(f'os times são : {times}')
print ('<->' * 15)
print(f'os primeiros colocados são {times[0:5]}')
print ('<->' * 15)
print(f'os 4 ultimos são{times[-4 :]}')
print ('<->' * 15)
print(f'em ordem alfabética será: {sorted(times)}')
print ('<->' * 15)
print(f'a posição do mirassol é {times.index("mirassol")}')