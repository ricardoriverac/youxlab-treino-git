print('\033[1;34m-=-=-=-=-= Valores únicos em uma lista =-=-=-=-=-\033[m')

lista = []

while True:
    numero = int(input('Digite um valor: '))
    if numero in lista:
        print('Valor duplicado, não irei adicionar...')
    else:
        print('Número cadastrado com sucesso!')
        lista.append(numero)

    
    escolha = str(input('Quer continuar? [S/N]: ')).upper()
    if escolha == 'N':    
            print('=-'*30)
            break
        
print(F'Você digitou os números: {sorted(lista)}')