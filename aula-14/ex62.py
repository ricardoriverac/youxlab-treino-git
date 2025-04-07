primter = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primter
contador = 1
total = 0
mostrados = 10
while mostrados != 0:
    total += mostrados
    while contador <= total: 
        print('{}'.format(termo), end = ' ')
        termo += razao
        contador += 1
    mostrados = int(input('\nVocê deseja que eu mostre mais quantos termos? '))
print('Finalizando...')