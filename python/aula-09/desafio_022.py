nome = str(input('Qual seu nome? ')).strip()
letras = len(nome) - nome.count(' ')
print(f'Seu nome tem: {letras} letras;')