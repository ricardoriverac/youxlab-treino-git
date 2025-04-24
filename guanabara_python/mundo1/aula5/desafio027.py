text = str(input('Digite seu nome: ')).strip()
nome = text.split()
fname = (nome[0])
lname = (nome[len(nome)-1])
print(f'''Seu primeiro nome é: {fname}
Seu último nome é: {lname}''')