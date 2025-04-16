mais18=0
homens=0
mulher20=0
while True:

    idade=int(input(' Qual a sua idade:'))
    sexo= ' '
    while sexo not in 'MF':
        sexo=str(input('qual seu sexo [M/F] ')).upper().strip()[0]

    if idade >=18:
        mais18 +=1
    if sexo=='M':
      homens +=1
    if idade < 20 and sexo =='F':
        mulher20+=1

    resposta=' ' 
    while resposta  not in'SN':
        resposta=str(input(' vc quer continuar? [S/N]')).upper().strip()[0]
    if resposta in'N':
        break

print(f'Existe {mais18} pessoas com mais de 18 anos.')
print(f'Existem ao todo {homens} homens cadastrados.')
print(f'Mulheres com menos de 20 anos = {mulher20}.')