isRodando = True
while isRodando:
    primeiroTermo = int(input('Digite o primeiro termo:'))
    razao = int(input('Digite a razão:'))
    cont = 1
    termo = primeiroTermo
    while cont <= 10:
        print(f'{termo} ', end= '')
        termo += razao
        cont += 1
    outroTermo = str(input('Quer ver mais termos? S/N:'))
    while outroTermo != 's':
        break
    else:
        more = int(input('Mais quantos termos?'))
        cont = 1
        while cont <= more:
            print(f'{termo} ', end= '')
            termo += razao
            cont += 1
