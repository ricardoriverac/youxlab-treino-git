#Primeiro nome e ultimo nome de uma pessoa

n = input("Digite seu nome completo: ")
nome = n.split()

print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format(nome[0]))
print("Seu ultimo nome é {}".format(nome[len(nome)-1]))