#Primeiro e último nome da pessoa
nome=str(input('Digite seu nome:' )).strip()
nomes=nome.split()#.split()--> comando que fatia palavras separando as as palavras 
print('Seu primeiro nome é: {}'.format(nomes[0]))
print('Seu ultimo nome é: {}'.format(nomes[len(nomes)-1]))
