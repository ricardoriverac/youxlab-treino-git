nome= str(input('Digite seu nome completo: ')) #criei uma variável do tipo string para inserir o nome
print('Analisando seu nome...') #printei na tela a frase anterior
print('Seu nome em maiúsculas é: {}'.format(nome.upper())) #printei o nome inserido em maiúsculas
print('Seu nome em minúsculas é: {}'.format(nome.lower())) #printei o nome inserido em minúsculas
nomeSemEspaços = len(nome)-nome.count(' ') #criei essa variável que analisa o comprimento do nome, conta cada letra sem os espaços e informa o número de letras sem contar os espaços
print('Seu nome tem ao todo {} letras sem os espaços'.format(nomeSemEspaços)) #printei o número de letras sem os espaços
nome1= nome.split() #dividi a variável nome em listas
primeiroNome= len(nome1[0]) #criei uma variável para contar o comprimento da string mas de apenas um elemento da lista nome1
print('Seu primeiro nome tem {} letras'.format(primeiroNome))  #printei a quantidade de letras do primeiro nome inserido