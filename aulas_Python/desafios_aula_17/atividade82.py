lista = []

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    
    escolha = str(input('Quer continuar? [S/N]: ')).upper()
    while escolha != 'S' and escolha != 'N':
        escolha = str(input(f'A opção que você escolheu "{escolha}" não funciona\n[S/N]: ')).upper()
        
    if escolha == 'N':
        sorted(lista)
        break
        
print('-='*40)
print(f'A lista completa é {lista}')
print('Os valores pares são:', [n for n in lista if n % 2 == 0], end=' ')
print('\nOs valores impares são:', [n for n in lista if n % 2 == 1], end=' ')
print()

