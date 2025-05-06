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
contadorbr = 0
contadorjp = 0 
contadorusa = 0
contadorfr = 0
contadorar = 0
somagolsbr = 0
somagolsjp = 0
somagolsusa = 0
somagolsfr = 0
somagolsar = 0
mediabr = 0
mediajp = 0
mediausa = 0
mediafr = 0
mediaar = 0
for jogador in jogadores:
    print(jogador['nacionalidade'])
    if jogador['nacionalidade'] == 'BR':
        contadorbr += 1
        somagolsbr += jogador['gols'] 
    if jogador['nacionalidade'] == 'JP':
        contadorjp += 1
        somagolsjp += jogador['gols'] 
    if jogador['nacionalidade'] == 'USA':
        contadorusa += 1
        somagolsusa += jogador['gols'] 
    if jogador['nacionalidade'] == 'FR':
        contadorfr += 1
        somagolsfr += jogador['gols'] 
    if jogador['nacionalidade'] == 'AR':
        contadorar += 1
        somagolsar += jogador['gols']
mediabr = somagolsbr / contadorbr
mediajp = somagolsjp / contadorjp
mediausa = somagolsusa / contadorusa
mediafr = somagolsfr / contadorfr
mediaar = somagolsar / contadorar
print ('-=' * 4, f'\033[35mQUANTIDADE DE JOGADORES POR NACIONALIDADE\033[m','-=' * 4 ) 
print(f'Brasil : {contadorbr}')
print(f'Japão : {contadorjp}')
print(f'USA : {contadorusa}')
print(f'França : {contadorfr}')
print(f'Argentina : {contadorar}')
print ('-=' * 4, f'\033[35mQUANTIDADE GOLS POR NACIONALIDADE\033[m','-=' * 4 )
print (f'Gols Brasil: {somagolsbr}')
print (f'Gols Japão: {somagolsjp}')
print (f'Gols USA: {somagolsusa}')
print (f'Gols França: {somagolsfr}')
print (f'Gols Argentina: {somagolsar}')
print ('-=' * 4, f'\033[35mMÉDIA POR NACIONALIDADE\033[m','-=' * 4 )
print (f'Média Brasil: {mediabr}')
print (f'Média Japão: {mediajp}')
print (f'Média USA: {mediausa}')
print (f'Média França: {mediafr}')
print (f'Média Argentina: {mediaar}')

    