#aprendendo modificaçao de textos
nome = str(input('Digite um nome: '))
#encontrar uma letra especifica
print(nome.find('A'))
#conta quantas letras existe
print(nome.count('A')+1)
#apaga os espaços do inicio e fim
print(nome.strip())
#contar quantos caracteres possui
print(len(nome))
#deixa em maiúsculas
print(nome.upper())
#deixa em minúsculas
print(nome.lower())