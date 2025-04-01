primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão de uma PA: '))
termo = primeiro
cont = 1
maisTermo = 10
total = 0
while maisTermo != 0 :
    total += maisTermo
    while cont <= total :
        print(f'{termo} -> ', end=' ')
        termo += razao
        cont += 1
    maisTermo = int(input('\nQuantos mais termos você quer mostrar: \033[32m[0]\033[m pra não mostrar mais nenhum '))
print(f'Finanlizado a progressão no total de {total} termos')
