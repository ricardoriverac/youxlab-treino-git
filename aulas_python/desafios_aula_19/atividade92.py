from datetime import datetime
ano_atual = datetime.now().year
dicionario = {}

print('\033[33m=-=\033[m'*15)

dicionario['Nome'] = str(input('Qual o seu nome?: '))

ano = int(input('Qual sua data de nascimento? (Apenas o ano): '))
idade = ano_atual - ano

dicionario['Carteira'] = int(input('Carteira de trabalho (0 = não tem): '))


if dicionario['Carteira'] == 0:
    print('\033[33m=-=\033[m'*15,f'\nO nome cadastrado é : {dicionario["Nome"]}')
    print(f'Sua idade é : {idade}')
    
else:
    AnoDeContratação = int(input('Qual o ano de contratação: '))
    dicionario['Salario'] = int(input('Qual o seu salario: R$'))
    
    print('\033[33m=-=\033[m'*15,f'\nO nome cadastrado é : {dicionario["Nome"]}')
    print(f'Sua idade é : {idade}')
    print(f'CTPS é: {dicionario["Carteira"]}')
    print(f'Seu salário é de: R${dicionario["Salario"]}')
    
    aposentadoria = AnoDeContratação + 35
    aposentadoria -= ano
    dicionario['aposentadoria'] = aposentadoria
    
    print(F'Você ira se aposentar com: {dicionario["aposentadoria"]} anos')
print('\033[33m=-=\033[m'*30)