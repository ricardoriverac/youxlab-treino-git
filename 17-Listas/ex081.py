lista = []
while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)

    escolha = str(input('Quer continuar? \n [S/N]: ')).upper()
    while escolha != 'S' and escolha != 'N':
        escolha = str(input(f'Não temos a opçao : {escolha}Quer continuar? [S/N]: ')).upper()
    if escolha == 'N':    
            break
    
    if 5 in lista:
        print('O valor 5 faz parte da lsita')
else:
    print('O valor 5 não faz parte da lista')

print(f'Você digitou {len(lista)} números')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')


