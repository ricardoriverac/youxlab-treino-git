print('Gerador de PA')
print('-=' * 10)
primeiroTermo= int(input('Primeiro termo: '))
razao= int(input('Razão da PA: '))
termo= primeiroTermo
contador= 1
while contador <= 10:
    print(f'{termo}'.format(end=''))
    termo += razao
    contador += 1
print('FIM!')