lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('\033[35mValor adicionado\033[m com sucesso! ')
    else:
        print('\033[33mValor duplicado!\033[m Não vou adicionar...')
    maisValores = input('Deseja continuar? \033[33m[S/N]\033[m').upper()
    if maisValores == 'S':
        continue
    elif maisValores == 'N':
        break
    elif maisValores != 'N' and maisValores != 'S':
        print('Erro na digitação! Tente novamente! ')
        maisValores = input('Deseja continuar? \033[33m[S/N]\033[m').upper()
        continue
ordem = sorted(lista)
print(f'Você digitou os valores {ordem}')