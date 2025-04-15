nome = input('Seu nome: ')
maiusculo = nome.upper()
min = nome.lower()
quantidade = len(nome) - nome.count(" ")
tamanho = len(nome)
print(f'''{maiusculo}
{min}
{quantidade}
{tamanho}''')