nome = input('Digite seu nome completo: ').strip()
primeiroeSegundoNome = nome.split()
print('Seu primeiro nome é {}'.format(primeiroeSegundoNome[0]))
print('Seu último nome é {}'.format(primeiroeSegundoNome[len(primeiroeSegundoNome)-1]))
