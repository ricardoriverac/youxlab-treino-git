n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
escolha = 0
while escolha != 5:
    print("""
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa""")
    
    print('\033[1;34m-=\033[m' * 13)
    escolha = int(input('Qual é sua escolha? '))
    print('\033[1;34m-=\033[m' * 13)

    #somando
    if escolha == 1:
       soma = n1 + n2
       print(f'A soma dos números é {soma}')

    #multiplicando
    if escolha == 2:
        print(f'O produto dos números é {n1 * n2}')

    #vendo quem é o maior
    if escolha == 3:
        if n1 > n2:
            print(f'O maior é {n1}')
        else:
            print(f'O maior é {n2}')

    #gerando novos numeros
    if escolha == 4:
        print('Escolha outros valores:')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))

#mensagem se apretar o 5
print('Fim do programa')