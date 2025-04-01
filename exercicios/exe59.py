#Crie um programa que leia dois valores e mostre um menu na tela:

#[1]Somar
#[2]Multiplicar
#[3]Maior
#[4]Novos números
#[5]Sair do Programa

#Seu programa deverá realizar a operação solicitada em cada caso.

programa = True

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
while programa:
    print('''Escolha uma opção: 
    [ 1 ] - Somar
    [ 2 ] - Multiplicação
    [ 3 ] - Maior
    [ 4 ] - Novos números
    [ 5 ] - Sair do programa\n''')
    
    pergunta = input("Qual opção acima voce deseja: ")

    if pergunta == "1":
        soma = numero1 + numero2
        resultado = soma

        print(f"O resultado da sua soma: {resultado}.\n")
    
    elif pergunta == "2":
        soma = numero1 * numero2
        resultado = soma

        print(f"O resultado da sua multiplicação: {resultado}\n")

    elif pergunta == "3":
        if numero1 > numero2:
            print(f"{numero1} é maior.")
        elif numero2 > numero1:
            print(f"{numero2} é maior.")
        elif numero1 == numero2:
            print("Os dois números são do mesmo tamanho.\n")

    if pergunta == "4":
        numero1 = int(input("Digite um número: "))
        numero2 = int(input("Digite outro número: "))

    if pergunta == "5":
        print("Você fechou o programa.")
        break
