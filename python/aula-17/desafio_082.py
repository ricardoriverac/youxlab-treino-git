par = list()
impar = list()
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r in 'nN':
        break
print(f'Na lista par contém os números {par}')
print(f'Na lista ímpar contém os números {impar}')
print(f'A lista completa é {par+ impar}')