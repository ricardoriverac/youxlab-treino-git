from time import sleep
tabela = ('Flamengo', 'Palmeiras', 'Ceará SC', 'Juventude', 'Fluminense', 'Vasco da Gama', 'Internacional', 'Fortaleza', 'Corinthias', 'Bota fogo', 'Bragantino', 'Cruzeiro', 'Grêmio', 'Bahia', 'São Paulo', 'Mirassol', 'Atlético-MG', 'Santos', 'EC Vitória', 'Sport Recife')
primeirosColocados = tabela[0:5]
ultimosColocados = tabela[16:]
ordemAlfabética = sorted(tabela)
posiçãoCruzeiro = tabela.index('Cruzeiro')

print('-='*20)
print('{:^30}'.format('\033[32mCAMPEONATO\033[m \033[33mBRASILEIRO\033[m \033[36mDE FUTEBOL\033[m'))
sleep(1)
print('-='*20)
print(tabela)
sleep(1)

print(f'''Os \033[36m5 PRIMEIROS\033[m colocados são: 
      {primeirosColocados} ''')
print('')
sleep(1)

print(f'''Os \033[35m4 ÚLTIMOS\033[m colocados na tabela são:
      {ultimosColocados}''')
print('')
sleep(1)

print(f'''A \033[32mORDEM ALFABÉTICA\033[m dos times da tabela é:
      {ordemAlfabética}''')
print('')
sleep (1)

print(f'''O \033[34mCRUZEIRO\033[m está na posição 
      {posiçãoCruzeiro+1}''')

