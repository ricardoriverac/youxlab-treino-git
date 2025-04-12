times = ('Cruzeiro', 'Flamengo', 'São Paulo', 'Internacional', 'Sport', 'Vasco', 'Juventude', 'Gremio',
         'Botafogo', 'Chapecoence', 'Bahia', 'Coritiba', 'Ponte preta', 'Santos', 'Mirasol', 'Vitoria', 'Fluminese', 'Avaí', 'Corinthians', 'Patetico_mineiro')
for t in times:
    print(t)
print('-=' *57)
print(f'Os 5 primeiros times são{times[0:5]}')
print('-=-'*38)
print(f'Os times rebaixados são {times[-4:]}')
print('-=-'*38)
print(f'Times em ordem alfabetica{sorted(times)}')
print('-=-'*38)
print(f'O pior time foi o Patetico mineiro {times.index("Patetico_mineiro")} posição.')
print('-=-'*38)
print(f'O time CAMPEÃO foi o {times[0]} Esporte Clube.')