c = cm = cf = cidd = 0
while True:
    se = ' '
    co = ' '
    print('='*10, 'cadastre-se', '='*10)
    no = str(input('fale seu nome: ')).strip()
    idd = int(input(f'qual a idade de {no} ? '))
    if idd > 18:
        cidd += 1
    while se not in 'MF':
        se = str(input(f'qual o sexo do(a) {no} [M/F]: ')).strip().upper()[0]
    if se == 'M':
        cm += 1
    elif se == 'F':
        if idd < 20:
            cf += 1
    while co not in 'SN':
        co = str(input('você deseja continuar [S/N]? ')).strip().upper()[0]
    if co == 'N':
        break
print('acabou. ')
print(f'Você cadastrou {cm} homens. Você cadastrou {cidd} pessoas maiores de 18 anos. Você cadastrou {cf} mulheres com menos de 20 anos.')