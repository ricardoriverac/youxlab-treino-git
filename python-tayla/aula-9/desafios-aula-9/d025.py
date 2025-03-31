nome = input('Qual é o seu nome? ').strip().capitalize()
existe = 'Silva' in nome
print(f'Seu nome é {nome[:]} então é verdade que têm Silva nele? {existe}')