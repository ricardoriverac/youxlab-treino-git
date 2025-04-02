#Crie um programa que simule o funcionamento de um caixa eletronico.
#No inicio, pergunte o usuario qual será o valor a ser sacado. (numero inteiro)
#E o programa vai informar quantas cedulas de cada valor serão entregues.

#Obs: Considere que o caixa possui cedulas de 50, 20, 10 e 1

valorDeSaque = int(input("Digite o valor do saque: "))

cedulas = [50, 20, 10, 1]
linhasLista = 0

while valorDeSaque > 0:
    cedulaAtual = cedulas[linhasLista]
    quantidade = valorDeSaque // cedulaAtual

    if quantidade > 0:
        print(f"Total de {quantidade} cédula(s) de R${cedulaAtual}.")

    valorDeSaque = valorDeSaque % cedulaAtual
    linhasLista += 1
