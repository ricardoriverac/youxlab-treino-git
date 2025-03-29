nome = str(input('Qual seu nome completo? ')).strip()

d = nome.split()
print('Seu primeiro nome é: {}'.format(d[0]))

d1 = nome.split()
print('Seu ultimo nome é: {}'.format(d1[-1]))