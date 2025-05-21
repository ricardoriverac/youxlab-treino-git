print('\033[1;34m-=-=-=-=-= Valores únicos em uma lista =-=-=-=-=-\033[m')

lista = []

while True:
    numero = int(input('Digite um valor: '))
    if numero in lista:
        print('\033[1;31mValor duplicado, não irei adicionar...\033[m')
    else:
        print('\033[1;32mNúmero cadastrado com sucesso!\033[m')
        lista.append(numero)

    
    escolha = str(input('Quer continuar? [S/N]: ')).upper()
    while escolha != 'S' and escolha != 'N':
        escolha = str(input(f'Não temos a opçao : {escolha}\nQuer continuar? [S/N]: ')).upper()
    if escolha == 'N':    
            print('=-'*30)
            break
        
print(F'Você digitou os números: {sorted(lista)}')