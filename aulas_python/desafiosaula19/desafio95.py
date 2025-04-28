# from time import sleep
# print('-='*20)
# print('\033[36mCADASTRO \033[32mDE JOGADOR\033[m \033[33mDE FUTEBOL\033[m')
# print('-='*20)
# jogador = {}
# lista = []
# time = []
# soma = 0
# while True:
#     jogador.clear()
#     jogador['nome'] = input('Nome: ')
#     jogador['partidas'] = int(input('Quantas partidas você jogou?: '))
#     lista.clear()
#     for c in range(0,jogador['partidas']):
#         gol = int(input(f'Quantos gols você fez na partida {c+1}?: '))
#         soma+=gol
#         lista.append(gol)
#     jogador['gol'] = lista
#     jogador['total'] = soma
#     time.append(jogador.copy())
#     print(time)
#     resp = input('Quer continuar? \033[33m[S/N]:\033[m ').upper()
    
#     while resp == 'SN':
#         break
#     if resp != 'S' and resp != 'N':
#         print('\033[31mErro na digitação!\033[m Tente novamente! ')
#         resp = input('Quer continuar? \033[33m[S/N]:\033[m ').upper()
#     if resp == 'N':
#         break
# print(f'{"COD NOME.":<10} {"GOLS ":<10} {"TOTAL ":>8}')
# print('-'*30)
# for k, v in enumerate(time):
#     print(f'{k} ', end='')
#     for i in v.values():
#         print(f'{str(i):>5}', end='')
#     print()
# print('-='*20)

from time import sleep
print('-='*20)
print('\033[36mCADASTRO \033[32mDE JOGADOR\033[m \033[33mDE FUTEBOL\033[m')
print('-='*20)

jogador = {}
time = []

while True:
    jogador.clear()
    jogador['nome'] = input('Nome: ')
    partidas = int(input('Quantas partidas você jogou?: '))
    gols = []
    total = 0

    for c in range(partidas):
        gol = int(input(f'Quantos gols você fez na partida {c+1}?: '))
        gols.append(gol)
        total += gol

    jogador['gols'] = gols
    jogador['total'] = total
    time.append(jogador.copy())

    while True:
        resp = input('Quer continuar? \033[33m[S/N]:\033[m ').strip().upper()
        if resp in ('S', 'N'):
            break
        print('\033[31mErro na digitação!\033[m Tente novamente!')

    if resp == 'N':
        break

print('-='*25)
print(f'{"COD":<4} {"NOME":<15} {"GOLS":<20} {"TOTAL":<5}')
print('-'*50)
for idx, jogador in enumerate(time):
    print(f'{idx:<4} {jogador["nome"]:<15} {str(jogador["gols"]):<20} {jogador["total"]:<5}')
print('-='*25)

while True:
    dados = int(input('Mostrar dados de qual jogador? \033[31m(999 interrompe):\033[m '))
    if dados == 999:
        print('\033[36mFINALIZANDO...\033[m')
        sleep(3)
        break
    if dados >= len(time):
        print(f'\033[31mERRO\033[m, não existe jogador com o códigos {dados}')
    else:
        print(f'MOSTRANDO DADOS DO JOGADOR \033[35m{time[dados]["nome"]}\033[m...')
        for i, g in enumerate(time[dados]["gols"]):
            print(f'   → Na partida {i+1}, fez {g} gols ')
            print(f'Foram um total de \033[1;36m{total[dados]} GOLS!\033[m ')
    print('-'*40)
print('\033[35mVOLTE SEMPRE!\033[m ')
