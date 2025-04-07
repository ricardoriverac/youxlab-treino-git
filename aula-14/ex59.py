n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
opcao = 0
while opcao != 5:
    print('''   -==-==-==-==-==-==-==-==-==-==-
    Aqui está um menu com as opções
    para você escolher o que você quer fazer
    com os números {} e {}.
    [ 1 ] Somar
    [ 2 ] Multiplicar 
    [ 3 ] O maior entre eles
    [ 4 ] Novos números
    [ 5 ] Sair do menu
    -==-==-==-==-==-==-==-==-==-==-'''.format(n1, n2))
    opcao = int(input('Qual opção você deseja? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
    elif opcao == 2:
        multipli = n1 * n2
        print('A multiplicação entre {} e {} dá {} '.format(n1, n2, multipli) )
    elif opcao == 3: 
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre os dois é o {} '.format(maior))
    elif opcao == 4:
        print('Informe os novos números.')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando o menu...')
    else:
        print('Opção inválida, tente novamente')

print('Obrigado por usar nosso menu! Volte sempre!')