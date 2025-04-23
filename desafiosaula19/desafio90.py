aluno = {}
aluno['Nome'] = input('Qual seu nome: ')
aluno['Média'] = float(input('Média de {}: '.format(aluno['Nome'])))
print('\033[35mNome\033[m é igual a {} '.format(aluno['Nome']))
print('\033[32mMédia\033[m é igual a {}'.format(aluno['Média']))
if aluno['Média'] < 7.0:
    print(f'{aluno["Nome"]} está \033[31mREPROVADO!\033[m ')
else:
    print(f'{aluno["Nome"]} está \033[36mAPROVADO!\033[m ')
