listaUm = []
listaDois = []
listaTres = []
while True:
    listaUm.append(int(input('Digite um valor: ')))
    maisValor = input('Deseja continuar? \033[33m[S/N]\033[m').upper()
    if maisValor == 'N':
        break
    elif maisValor != 'N' and maisValor != 'S':
        print('Erro na digitação! Tente novamente! ')
        maisValor = input('Deseja continuar? \033[33m[S/N]\033[m').upper()
for num in listaUm:
    if num % 2 == 0:
        listaDois.append(num)
for num in listaUm:
    if num % 2 == 1:
        listaTres.append(num)
print(f'A \033[34mlista completa\033[m é {listaUm}')
print(f'A \033[32mlista de pares\033[m é {listaDois}')
print(f'A \033[35mlista de ímpares\033[m é {listaTres}')
