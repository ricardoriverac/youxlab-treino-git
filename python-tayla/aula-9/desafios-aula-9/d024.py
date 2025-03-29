cidade = input('Qual o nome da sua cidade? ').strip().capitalize()
existe = 'Santo' in cidade
print(f'O começo da sua cidade é {cidade[:6]} então é verdade que começa com Santo? {existe}')