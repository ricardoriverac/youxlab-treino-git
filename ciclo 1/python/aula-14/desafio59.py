from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('=-='*10)
opcao = 0
while opcao != 5:
    print('[1] Somar'
          '\n[2] Multiplicar'
          '\n[3] Maior'
          '\n[4] Novos Números'
          '\n[5] Sair do Programa')
    opcao = int(input('>>> Qual sua opção: '))
    if opcao == 1:
        print(f'A soma de {n1} + {n2} é {n1+n2}')
        print('=-='*10)
    if opcao == 2:
        print(f'O resultado de {n1} x {n2} é {n1*n2}')
        print('=-='*10)
    if opcao == 3:
        print(f'Entre {n1} e {n2} ',end='')
        if n1 == n2:
            print('os valores são iguais.')
        else:
            lista = n1, n2
            print(f'o MAIOR é {max(lista)}')
        print('=-='*10)
    if opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=-='*10)
    if opcao == 0 or opcao > 5:
        print('Opção Inválida. Tente novamente')
        print('=-='*10)
print('Finalizando',end='')
for c in range(0,5):
    print('.',end=''),sleep(0.5)
print('\nFim do Programa! Volte Sempre!')