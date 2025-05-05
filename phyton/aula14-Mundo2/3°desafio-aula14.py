#MENU DE OPÇÕES
numero1=int(input('Digite o 1° nùmero:'))
numero2=int(input('Digite o 2° número:'))
escolha=0
while escolha != 5:
    print('1- somar\n2- multiplicar\n3- maior\n4- novos números\n5- sair')
    escolha=int(input('Qual é a sua opção?:'))
    if escolha==1:
        soma=numero1+numero2
        print(f'A soma dos dois valores é:{soma}')
    if escolha==2:
        multiplica=numero1*numero2
        print(f'A multiplicação dos dois valores é:{multiplica}')
    if escolha==3:
        if numero1>numero2:
            print(f'O maior número é o {numero1}')
        if numero1==numero2:
            print('Os dois números são iguais')
        elif numero2>numero1:
            print(f'O maior número é o {numero2}')
    if escolha==4:
        numero1=int(input('Digite o 1° nùmero:'))
        numero2=int(input('Digite o 2° número:'))
    if escolha==5:
        break



    

