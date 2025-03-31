n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print("""-=-=-=-=-=-=-=
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA!""")
    opcao = int(input('Qual é a sua opção: '))
    if opcao == 1:
        s = n1 + n2
        print(f'A soma dos valores {n1} + {n2} foi {s}')
    elif opcao == 2 :
        m = n1 * n2
        print(f'A multiplicação de {n1} e {n2} foi {m}')
    elif opcao == 3 :
        if n1 > n2 :
            print(f'O maior valor foi o \033[31mprimeiro valor\033[m {n1}')
        elif n2 > n1 :
            print(f'O maior valor foi o \033[31msegundo valor\033[m {n2}')
    elif opcao == 4 :
        print('Informe os novos números')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
print('Fim do programa')
    

