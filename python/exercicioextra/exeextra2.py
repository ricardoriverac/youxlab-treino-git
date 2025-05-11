# faça um programa que leia a nacionalidade de vários jogador , é faça a media da nacionalidade deles, é mostre o nome do jogador que fez mais gol da sua nacionalidade

def linha(tam=42):
    return '-' * tam
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

#programa principal
dados_do_jogador = {}
dados_dos_jogadores = []
paises = []
while True:
    jogador = str(input('Digite o nome do jogador: '))
    nacionalidade = str(input('Digite a nacionalidade: ')).upper().strip()
    gols = int(input('Quantos gols ele fez: '))
    dados_do_jogador['jogador'] = jogador
    dados_do_jogador['nacionalidade'] = nacionalidade
    dados_do_jogador['gols'] = gols
    dados_dos_jogadores.append(dados_do_jogador.copy())
    dados_do_jogador.clear()
    sair = str(input('Quer Adicionar mais alguém [S/N]: ')).upper().strip()
    if sair == 'N':
        break
for jogador in dados_dos_jogadores:
    if jogador['nacionalidade'] not in paises:
        paises.append(jogador['nacionalidade'])
cabecalho('Média dos países')
for pais in paises:
    nacionalidade_do_jogadores = []
    for na in dados_dos_jogadores:
        if na['nacionalidade'] == pais:
            nacionalidade_do_jogadores.append(na)
    soma = 0
    for gol in nacionalidade_do_jogadores:
        soma += gol['gols']
        calculamedia = soma / len(nacionalidade_do_jogadores)
    print(f'{pais} a média desse país é {calculamedia}')

print(nacionalidade_do_jogadores)
print(paises)
print(dados_dos_jogadores)
print(jogador)
print(nacionalidade)
print(gols)