times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará',
         'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('-='*20)
print(f'A lista de times do Brasileirão:{times}')
print('-='*20)
print(f'os primeiros 5 colocados foram:{times[0:5]}')
print('-='*20)
print(f'Os times que vão para a fase de grupo para a libertadores '
      f'são: {times[0:6]}')
print('-='*20)
print(f'os dois times que vão para a primeira fase da libertadores '
      f'são: {times[6:8]}')
print('-='*20)
print(f'Os times da sulamericana são {times[8:14]}')
print('-='*20)
print(f'Os times rebaixados foram{times[16:]}')
print('-='*20)
print(f'os times em ordem alfabética {sorted(times)}')
print('-='*20)
print(f'A chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('-='*20)