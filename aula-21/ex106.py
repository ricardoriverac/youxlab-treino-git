def titulo(txt):
    a = len(txt)
    print('~'* a * 2)
    print(txt.center(a*2))
    print('~'* a * 2)
    print()

def h():
    while True:
        titulo('\033[1;101mSISTEMA DE AJUDA PyHelp\033[m')
        c = str(input('Função ou biblioteca > '))
        if c == 0:
            break
        print()
        titulo(f'\033[1;104mAcessando manual do {c}...\033[m')
        help(c)
h()