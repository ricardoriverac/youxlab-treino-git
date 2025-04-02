nome = str(input('Insira seu nome completo; ')).strip()
m = nome.upper()
mi = nome.lower()
n = len (nome)-nome.count(" ")
p =len(nome)
n2 = nome.find(" ")
print("Analisando seu nome...")
print("O nome {}, em Maisculo vai ficar {}".format(nome,m))
print('Seu nome em Minusculas vai ficar {}'.format(mi))
print("Seu nome tem {}, letras ".format(n))
print("Seu primeiro nome tem {},".format(n2))



