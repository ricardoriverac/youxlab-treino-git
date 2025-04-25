lista = []

while True:
    armazem = {}
    listaDeGol = []
    
    armazem['Nome'] = str(input('Qual o nome do jogador?: '))
    partidas = int(input(f'Quantas partidas {armazem["Nome"]} jogou?: '))
    
    
    for v in range(1, partidas +1):
        Gols = int(input(f'  Quantos gols {armazem["Nome"]} fez na partida {v}: '))
        listaDeGol.append(Gols)
        
    armazem['Gols Feitos'] = listaDeGol
    armazem['Total de gols'] = sum(listaDeGol)
    lista.append(armazem.copy())
    
    escolha = str(input('Quer continuar? [S/N]: ')).upper()
    while escolha not in ['S', 'N']:
        escolha = str(input(f'\033[31mNão temos a opção "{escolha}"\n\033[33m[S/N]: \033[m')).upper()

    if escolha == 'N':
        break

print('\033[36m-=\033[m'*30)
print(f'\033[1;37m{"No.":<4}{"Nome":<15}{"Gols":<20}{"Total":>6}\033[m')
print('\033[36m-\033[m'*30)

for i, jogador in enumerate(lista):
    print(f'{i:<4}{jogador["Nome"]:<15}{str(jogador["Gols Feitos"]):<20}{jogador["Total de gols"]:>6}')

while True:
    print('\033[36m-\033[m'*30)
    opc = int(input('Mostrar dados de qual jogador? (999 para o programa): '))
    if opc == 999:
        print('\033[31mEncerrando...\033[m')
        break    
    if 0 <= opc < len(lista):
        print(f'\033[1;33mLevantamenti do jogador {lista[opc]["Nome"]}:\033[m')
        for o, g in enumerate(lista[opc]["Gols Feitos"]):
            print(f'     No jogo {o+1} fez {g} gols')
            
    else:
        print(f'\033[31mJogador {opc} não encontrado. Tente novamente!!\033[m')
print('\033[1;32m=-=-=-= VOLTE SEMPRE =-=-=-=\033[m')