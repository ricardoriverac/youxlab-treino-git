#Analise de nome
Nome=str(input('Digite o nome completo:')).strip()
print('Analisando...')
print('Seu nome em letras maiúsculas:{}'.format(Nome.upper()))
print('Seu nome em letras minúsculas:{}'.format(Nome.lower()))
print('Seu nome inteiro tem {} letras '.format(len(Nome) - Nome.count(' ')))
print('Seu 1° nome tem {} letras'.format(Nome.find(' ')))