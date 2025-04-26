def ficha(NomeJogador='<desconhecido>',QuantidadeGols=0):
    print(f'O jogador {NomeJogador} marcou {QuantidadeGols} gol(s) no campeonato.')
print('\n' + '\033[35m-\033[m'*40)
NomeDigitado=input("Nome do jogador: ").strip()
print('\n' + '\033[35m-\033[m'*40)
GolsDigitados=input("Número de gols: ").strip()
print('\n' + '\033[35m-\033[m'*40)
if GolsDigitados.isnumeric():
    QuantidadeGols=int(GolsDigitados)
else:
    QuantidadeGols=0
if NomeDigitado=='':
    ficha(QuantidadeGols=QuantidadeGols)
else:
    ficha(NomeJogador=NomeDigitado,QuantidadeGols=QuantidadeGols)