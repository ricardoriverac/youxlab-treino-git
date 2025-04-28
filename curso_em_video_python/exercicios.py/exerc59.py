valor1 = int(input('Digite o 1° valor: '))
valor2 = int(input('Digite o 2° valor: '))
opcao = 0
while opcao!=6:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Dividir')
    print('[5] Novos números')
    print('[6] Sair do programa')
    opcao = int(input('Escolha uma opção: '))
    if opcao ==5:
        valor1 = int(input('Digite o 1° valor: '))
        valor2 = int(input('Digite o 2° valor: '))
    if opcao == 1:
        print('A soma entre os dois é: {}'.format(valor1 + valor2))
    elif opcao == 2:
        print('A multiplicação entre os dois é: {}'.format(valor1 * valor2))
    elif opcao ==3:
        lista =[valor1, valor2]
        maior = max(lista)
        print('O maior número entre os dois é: {}'.format(maior))
    elif opcao==4 :
        print('A divisão entre os dois é {:.2}'.format(valor1 / valor2))
print ('OBRIGADA POR PARTICIPAR!')
    
