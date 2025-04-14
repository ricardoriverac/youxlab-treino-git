primeiroTermo= int(input('Primeiro termo: '))
razao= int(input('Razão: '))
ultimoTermo= primeiroTermo + (10 - 1) * razao
for a in range(primeiroTermo, ultimoTermo+1, razao):
    print('{}° > '.format(a), end='')
