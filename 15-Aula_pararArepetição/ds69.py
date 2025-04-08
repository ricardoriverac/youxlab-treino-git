tot18 =totH =totM20 =0
while True:
    idade = int(input('idade: '))
    sexo =' '
    while sexo not in 'MF':
        sexo =str(input('Sexo: [M/F] '))
    if idade >= 18:
        tot18+=1
    if sexo == 'M':
        totH+=1
    if sexo == 'F' and  idade < 20:
        totM20 += 1
    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar ? [S/N] '))
    if resp == 'N':
        break
print(f'Pessoas maior de 18 : {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} de mulheres com menos de 20')
