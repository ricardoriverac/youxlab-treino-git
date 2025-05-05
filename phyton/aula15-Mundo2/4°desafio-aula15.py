#ANÀLISE DE DADOS DO GRUPO
contIdade=contHomem=contMulher=0
while True:
    print('Cadestre uma pessoa.')
    idade=int(input('Digite a idade: '))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('Digite o sexo [M/F]:')).strip().upper()[0]
    if idade>18:
        contIdade+=1
    if sexo=='M':
        contHomem+=1
    if sexo=='F' and idade<20:
        contMulher+=1
    escolha=' ' 
    while escolha not in 'SN':
        escolha=str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha=='N':
        break
print(f'{contIdade} pessoas tem mais de 18 anos, {contHomem} homens foram cadastrados e {contMulher} mulher com menos de 20 anos')