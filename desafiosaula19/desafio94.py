from time import sleep
print('-='*20)
print('{:^30}'.format('\033[35mCADASTRO\033[m'))
print('-='*20)
lista = []
pessoa = {}
cadastro = soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    
    while True:
        pessoa['sexo'] = input('Qual seu sexo? \033[33m[F/M]:\033[m ').upper()
        if pessoa['sexo'] in 'MF':
            break
        print('Erro na digitação! Tente novamente! ')
    pessoa['idade'] = int(input('Idade: '))
    soma+=pessoa['idade']
    lista.append(pessoa.copy())
    cadastro+=1
    resp = input('Quer continuar? \033[33m[S/N]:\033[m ').upper()
    
    while resp == 'SN':
        break
    if resp != 'S' and resp != 'N':
        print('\033[31mErro na digitação!\033[m Tente novamente! ')
        resp = input('Quer continuar? \033[33m[S/N]:\033[m ').upper()
    if resp == 'N':
        print('-='*20) 
        print('    \033[36mFINALIZANDO PROGRAMA...\033[m ')
        sleep(3)
        break
media = soma/cadastro
print('-='*20) 
print(lista)
print(f'Ao todo temos {cadastro} \033[35mpessoas cadastradas\033[m ')
print(f'A \033[34mmédia das idades\033[m é {media:5.2f} ')

print('As \033[32mmulheres cadastradas\033[m foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='')
print()
print('As pessoas com \033[36midade acima da idade média\033[m são: ', end='')
for p in lista:
    if p['idade'] > media:
        print(f'{p["nome"]}')
print()
