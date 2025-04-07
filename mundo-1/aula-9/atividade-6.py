n = str(input('Qual e seu nome? ')).strip()
nome = n.split()
print('Seu nome é {}'.format(nome[0]))
print('Seu sobrenome é {}'.format(nome[len(nome)-1]))