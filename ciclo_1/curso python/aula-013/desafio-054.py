from datetime import datetime
ano_Atual = datetime.now().year
c = 0
for i in range(1, 7 +1):
    nomes = int(input('Digite o ano de nascimento:'))
    idade = ano_Atual - nomes
    if idade <= 18:
        print('Esse ainda não é maior de idade.')
        c += 1
        print('{} pessoas são menores de idade.'.format(c))
    else:
        print('Esse ja é de maior')
