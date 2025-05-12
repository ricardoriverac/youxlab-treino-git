from time import sleep

def JP():
    soma=0
    cont_jogador=0
    j=0
    for nac in jogadores:
        if  nac['nacionalidade'] =='JP':
            soma+=nac['gols']
            cont_jogador+=1
            j=soma/cont_jogador
    print(j)
def USA():
    soma=0
    cont_jogador=0
    j=0
    for nac in jogadores:
        if  nac['nacionalidade'] =='USA':
            soma+=nac['gols']
            cont_jogador+=1
            j=soma/cont_jogador
    print(j)     
def FR():
    soma=0
    cont_jogador=0
    j=0
    for nac in jogadores:
        if  nac['nacionalidade'] =='FR':
            soma+=nac['gols']
            cont_jogador+=1
            j=soma/cont_jogador
    print(j)     
def AR():
    soma=0
    cont_jogador=0
    j=0
    for nac in jogadores:
        if  nac['nacionalidade'] =='AR':
            soma+=nac['gols']
            cont_jogador+=1
            j=soma/cont_jogador
    print(j)          

paim = [
    {"nacionalidade": "BR"},
    {"nacionalidade": "JP"},
    {"nacionalidade": "USA"},
    {"nacionalidade": "FR"},
    {"nacionalidade": "AR"}
]

jogadores = [
    {"nome": "Ricardo", "gols": 5, "nacionalidade": "BR"},
    {"nome": "Walter", "gols": 7, "nacionalidade": "BR"},
    {"nome": "Japa", "gols": 12, "nacionalidade": "JP"},
    {"nome": "Joao", "gols": 9, "nacionalidade": "JP"},
    {"nome": "Augusto", "gols": 2, "nacionalidade": "USA"},
    {"nome": "Cesar", "gols": 5, "nacionalidade": "USA"},
    {"nome": "Kaio", "gols": 2, "nacionalidade": "JP"},
    {"nome": "Lucas", "gols": 4, "nacionalidade": "BR"},
    {"nome": "Felipe", "gols": 8, "nacionalidade": "BR"},
    {"nome": "Takeshi", "gols": 6, "nacionalidade": "JP"},
    {"nome": "Yuki", "gols": 10, "nacionalidade": "JP"},
    {"nome": "Max", "gols": 3, "nacionalidade": "USA"},
    {"nome": "Julien", "gols": 7, "nacionalidade": "FR"},
    {"nome": "Pierre", "gols": 5, "nacionalidade": "FR"},
    {"nome": "Emiliano", "gols": 2, "nacionalidade": "AR"},
    {"nome": "Ricardo Jr.", "gols": 9, "nacionalidade": "BR"},
    {"nome": "Santos", "gols": 1, "nacionalidade": "BR"},
    {"nome": "Gabriel", "gols": 3, "nacionalidade": "USA"},
    {"nome": "Mauricio", "gols": 6, "nacionalidade": "AR"}
]
soma=0
cont_jogador=0
for jogador in jogadores:
    print(jogador['nome'] , jogador['nacionalidade'])
    print("O numero de gols desse jogador foi:",  jogador['gols'])
    print('-='*7)
print('-=' *10)
for nac in jogadores:
    if  nac ==jogador:
        soma+=nac['gols']
        cont_jogador+=1
print('='* 25)
print('A Media de gols do Brasil foi...')
print('='* 25)
sleep(1)
t=int(soma/cont_jogador)
print(t)

print('='* 25)
print('A Media de gols do Japão foi...')
print('='* 25)
sleep(1)
JP()

print('='* 25)
print('A Media de gols do EUA foi...')
print('='* 25)
sleep(1)
USA()

print('='* 25)
print('A Media de gols da Argentina foi...')
print('='* 25)
sleep(1)
AR()

print('==' * 30)
print(f'{"NOME":<10}{"MEDIA DE GOLS":>8}')
print('-'*30)
