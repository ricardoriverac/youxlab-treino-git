from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

opcao = 0
while opcao != 5:
    print('\n----- MENU -----')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')

    opcao = int(input('>>>>> Qual é a sua opção? '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O produto de {n1} e {n2} é {produto}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n2 > n1:
            print(f'O maior número é {n2}')
        else:
            print('Os dois números são iguais.')
    elif opcao == 4:
        n1 = int(input('Digite o novo primeiro número: '))
        n2 = int(input('Digite o novo segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    
    sleep(1)

print('Fim do programa! Volte sempre :)')