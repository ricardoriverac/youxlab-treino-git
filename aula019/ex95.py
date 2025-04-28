jogador = {}
contador = 0
gols = []
soma = 0
time = []  

while True:
    jogador.clear()
    gols.clear()  
    contador = 0  

    escolha = str(input('Deseja continuar: [S/N] ').upper())

    if escolha == 'N':
        break

    jogador['nome'] = str(input('Digite o nome do jogador: '))
    total = int(input('Quantas partidas o jogador jogou?: '))

    while contador != total:
        contador += 1
        gols.append(int(input(f'Digite quantos gols fez no {contador} jogo: ')))

    jogador['soma'] = sum(gols)
    jogador['gols'] = gols.copy() 

    time.append(jogador.copy())  

    print(jogador)

    for partida_numero, pontos in enumerate(jogador['gols']):
        print(f'--- Na partida {partida_numero + 1} fez {pontos} gols ')

for index in jogador.keys():
    print(f'{index:<5}', end = '')

    print( )


print( '-'*50)
print(f'{"cod":<5}{"nome":<15}{"gols":<20}{"total":<5}')
print('-'*50)




for codigo, jogador in enumerate(time):
    print(f'{codigo:<5}{jogador["nome"]:<15}{str(jogador["gols"]):<20}{jogador["soma"]:<5}')

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break

    




