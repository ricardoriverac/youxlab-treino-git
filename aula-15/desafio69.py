c = cm = cf = cidd = 0
while True:
    se = ' '
    co = ' '
    print('='*10, 'CADASTRO', '='*10)
    no = str(input('Digite um nome: ')).strip().upper()
    idd = int(input(f'Digite a idade de {no} agora: '))
    if idd > 18:
        cidd += 1
    while se not in 'MF':
        se = str(input(f'Digite o sexo de {no} [M/F]: ')).strip().upper()[0]
    if se == 'M':
        cm += 1
    elif se == 'F':
        if idd < 20:
            cf += 1
    while co not in 'SN':
        co = str(input('Você deseja continuar [S/N]? ')).strip().upper()[0]
    if co == 'N':
        break
print('='*10, 'FIM DO PROGRAMA', '='*10)
print(f'Você cadastrou {cm} homens. \nVocê cadastrou {cidd} pessoas maiores de 18 anos. \nVocê cadastrou {cf} mulheres com menos de 20 anos.')