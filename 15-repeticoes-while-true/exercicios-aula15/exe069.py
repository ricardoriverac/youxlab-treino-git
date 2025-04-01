mais18 = 0
totalH = 0
mulheres = 0
while True:
    idade = int(input('Digite sua idade: '))
    if idade >= 18 :
        mais18 += 1
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        while True:
            sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
            if sexo == 'M' or sexo == 'F' :
                if sexo == 'M':
                    break
    if sexo == 'M' :
        totalH += 1
    if sexo == 'F' :
        if idade < 20:
            mulheres += 1
    opcao = str(input('Quer continuar [S/N] ')).upper().strip()
    if opcao != 'S' and opcao != 'N':
        while True:
            opcao = str(input('Quer continuar [S/N] ')).upper().strip()
            if opcao == 'S' or opcao == 'N':
                break
    if opcao == 'N' :
        break
print(f'Total de homens cadastrados foi {totalH}')
print(f'Total de pessoas com mais de 18 anos:{mais18}')
print(f'Total de mulheres com menos de 20 foi {mulheres}')

