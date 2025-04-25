def áreat(l, c):
    area = l * c

    print('\n' + '\033[35m-\033[m'*40)
    print ('-=' * 4, f'\033[35m« controle de terrenos »\033[m','-=' * 4 )
    print(f'A área do terreno ({l}m x {c}m) é de {area} m².')
l = float(input('Digite a largura do terreno (em metros): '))
c = float(input('Digite o comprimento do terreno (em metros): '))
áreat(l, c)