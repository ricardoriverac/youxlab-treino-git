print ("\t-----" * 4)
PrimeiroNumero = int (input ("Digite um número : "))
print ("\t-----" * 4)
SegundoNumero = int (input ("Digite outro número : "))
opcao = 0
while opcao !=  5:
    print ("\t-----" * 4)
    print ("<<<<<<<<<< MENU >>>>>>>>>>")

    print("""
    [1] SOMAR. 
    [2] MULTIPLICAR.
    [3] MAIOR.
    [4] NOVOS NÚMEROS.
    [5] SAIR DO PROGRAMA.
        """)
    print ("\t-----" * 4)
    opcao = int (input ("Digite sua opção: "))
    print ("\t-----" * 4)
    if opcao == 1:
        soma = PrimeiroNumero + SegundoNumero
        print ("A soma entre o número {} e o número {}, é = {}.".format(PrimeiroNumero,SegundoNumero,soma))
    elif opcao == 2: 
        multiplicação = PrimeiroNumero * SegundoNumero
        print ("A multiplicação entre o número {} e o número {}, é = {}.".format(PrimeiroNumero,SegundoNumero,multiplicação))
    elif opcao == 3:
        if  PrimeiroNumero > SegundoNumero:
            maior = PrimeiroNumero
            print ("entre o número {} e o número {}, o maior é {}.".format(PrimeiroNumero,SegundoNumero,maior))
        else:
            maior = SegundoNumero
            print ("entre o número {} e o número {}, o maior é {}.".format(PrimeiroNumero,SegundoNumero,maior))
    elif opcao == 4:
        print ("Informe os números novamente>>")
        PrimeiroNumero = int (input ("Digite um número : "))
        SegundoNumero = int (input ("Digite outro número : "))
    elif opcao == 5:
        print ("ATÉ LOGO")
    else:
        print ("Opção inválida!!")
print ("FIM, você saiu do programa!!")

