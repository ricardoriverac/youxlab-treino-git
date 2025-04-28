print('Gerador de PA')
print('-=' * 10)
primeiroTermo= int(input('Primeiro termo: '))
razao= int(input('Razão da PA: '))
termo= primeiroTermo
contador= 1
total= 0
mais= 10
while mais != 0:
    total= total + mais
    while contador <= total:
        print(f'{termo}'.format(end=''))
        termo += razao
        contador += 1
    print('PAUSA...')
    mais= int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')