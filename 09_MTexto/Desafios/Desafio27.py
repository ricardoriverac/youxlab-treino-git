n1 = str(input("Insira seu nome completo: ")).strip()
nome = n1.split()
print("Muito prazer em te conhecer! {}".format(n1))
print("Seu primeiro nome e {}".format(nome[0]))
print("Seu ultimo nome e {}".format(nome[len(nome)-1]))