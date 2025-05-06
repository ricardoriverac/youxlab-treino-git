numero1= int(input('Primeiro valor: '))
numero2= int(input('Segundo valor: '))
soma= 0
multiplicacao= 0
maior= 0
novos_numeros= 0
sair_do_programa=0 
opcao= 0
while opcao != 5:
    print(' [1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa') 
    opcao= int(input('Qual é sua escolha? ')) 
    if opcao == 1:
        soma= numero1 + numero2
        print(f'Resultado da soma de {numero1} + {numero2}: {soma}')

    elif opcao == 2:
            multiplicacao= numero1 * numero2
            print(f'Resultado da multiplicação de {numero1} e {numero2}: {multiplicacao}')

    elif opcao == 3:
            if numero1 > numero2:
                maior= numero1
                print(f'{maior} é o maior número.')
            else:
             maior= numero2 
             print(f'{maior} é o maior número.')
    elif opcao == 4:
         print('Informe os números novamente:')
         numero1= int(input('Primeiro valor: '))
         numero2= int(input('Segundo valor: '))
    elif opcao == 5:
        print('FINALIZANDO...')
    else:
         print('Opção inválida!')         
print('Fim do programa. Volte sempre!')