print('\033[1;34m-=-=-=-=-= Menu de Opções =-=-=-=-=-\033[m')

numero1 = int(input('Digite o primeiro número '))
numero2 = int(input('Digite o segundo número '))
while True:
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    opcao = int(input('Qual sua opção? '))

    if opcao == 1:
        resultado1 = (numero1+numero2)
        print(resultado1)
        
    elif opcao == 2:
        resultado2 = (numero1*numero2)
        print(resultado2)
        
    elif opcao == 3:
        resultado3 = max(numero1, numero2)
        print(resultado3)
        
    elif opcao == 4:
        numero1 = int(input('Digite o primeiro número '))
        numero2 = int(input('Digite o segundo número '))
        
    elif opcao == 5:
        print('Programa encerrado!')
        break
    
    #JEITO ACIMA TA CERTO POREM O "WHILHE TRUE E BRECK N É LEGAL USAR ENTAO FAÇA ASSIM :
# print('\033[1;34m-=-=-=-=-= Menu de Opções =-=-=-=-=-\033[m')

# numero1 = int(input('Digite o primeiro número '))
# numero2 = int(input('Digite o segundo número '))
# seila = True
# while seila == True:
#     print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
#     opcao = int(input('Qual sua opção? '))

#     if opcao == 1:
#         resultado1 = (numero1+numero2)
#         print(resultado1)
        
#     elif opcao == 2:
#         resultado2 = (numero1*numero2)
#         print(resultado2)
        
#     elif opcao == 3:
#         resultado3 = max(numero1, numero2)
#         print(resultado3)
        
#     elif opcao == 4:
#         numero1 = int(input('Digite o primeiro número '))
#         numero2 = int(input('Digite o segundo número '))
        
#     elif opcao == 5:
#         print('Programa encerrado!')
#         seila = False