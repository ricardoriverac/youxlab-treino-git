lista = []
cont = 0 
while True:
    numero = int(input('Digite um valor: '))
    cont += 1
    lista.append(numero)
    
    escolha = str(input('Quer continuar? [S/N]: ')).upper()
    while escolha != 'S' and escolha != 'N':
        escolha = str(input(f'A opção que você escolheu "{escolha}" não funciona\n[S/N]: ')).upper()
        
    if escolha == 'N':
        break
    
print(f'---------------------------------------\nVocê digitou "{cont}" números.')
print(F'Os valores em ordem decrescente são: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O número 5 estava na lista!')
    
else:
    print('O número 5 não estava na lista!')