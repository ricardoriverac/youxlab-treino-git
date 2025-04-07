maisde18 = homens = mulhermenosde20 = contagem = mulheres =  0

while True:
    print('-'*35)
    print('           CADASTRANDO')
    print('-'*35)
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]:')).strip().upper()[0]
    continuar = str(input('DESEJA CONTINUAR? [S/N]')).strip().upper()[0]
    contagem +=1
    if idade > 18:
        maisde18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        mulheres += 1
        if idade < 20:
            mulhermenosde20 += 1
        
    if continuar == 'N':
        break
print('-='*30)
print(f'Foram cadastrados {maisde18} pessoas com mais de 18 anos.')
print(f'Das {contagem} pessoas que foram cadastrados, {homens} eram homens.')
print(f'Das {mulheres} mulheres que foram cadastradas, {mulhermenosde20} tem menos de 20 anos.') 