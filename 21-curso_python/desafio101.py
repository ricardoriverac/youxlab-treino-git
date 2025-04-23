from datetime import date
anoAtual = date.today().year
texto = 'VAMOS VER SE SEU VOTO É \033[1;31mNEGADO\033[m, \033[1;33mOPCIONAL\033[m ou \033[1;32mOBRIGATÓRIO\033[m'

def linha():
    print('=' * 55)
    print(texto)
    print('=' * 55)

linha()

nascimento = int(input('\033[1mQual seu ano de nascimento?\033[m '))
idade = anoAtual - nascimento


def voto(ano):
    if idade < 16:
        print('Você ainda \033[1;31mnão pode votar\033[m!! ')
    if idade >=16 and idade <=17:
        print('O seu voto ainda é \033[1;33mOPCIONAL\033[m!')
    if idade  >= 18:
        print('O seu voto é \033[1;32mOBRIGATÓRIO\033[m!')

voto(nascimento)