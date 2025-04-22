galera = list()
dado = list()
maiorPeso = menorPeso = cadastro = media = soma = 0
while True:
    dado.append(input('Nome: '))
    dado.append(float(input('Peso: ')))
    soma+=dado[1]
    if len(galera) == 0:
        maiorPeso = menorPeso = dado [1]
    else:
        if dado [1] > maiorPeso:
            maiorPeso = dado [1]
        if dado [1] < menorPeso:
            menorPeso = dado [1]
    galera.append(dado[:])
    dado.clear()
    maisCadastro = input('Quer continuar? \033[33m[S/N]\033[m: ').upper()
    cadastro += 1
    
    if maisCadastro == 'N':
        break
    elif maisCadastro != 'N' and maisCadastro != 'S':
        print('Erro na digitação! Tente novamente! ')
        maisCadastro = input('Quer continuar? \033[33m[S/N]\033[m: ').upper()
    elif maisCadastro == 'S':
        continue
print(f'{cadastro} pessoas foram \033[36mCADASTRADAS\033[m ')

print(f'O \033[35mMAIOR PESO\033[m foi de {maiorPeso}KG. Peso de ', end='')
for n in galera:
    if n [1] == maiorPeso:
        print(f'{n[0]}')
print(f'O \033[34mMENOR PESO\033[m foi de {menorPeso}KG. Peso de ', end='')
for n in galera:
    if n [1] == menorPeso:
        print(f'{n[0]}')
media = soma/cadastro
print(f'A \033[32mMÉDIA\033[m dos pesos é {media:.2f}')