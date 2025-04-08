from datetime import date
anoAtual = date.today().year
contadorMaiorIdade = 0
contadorMenorIdade = 0
for c in range (0,3):
    idade = int (input("Digite sua idade: "))
    if idade < 18:
        print ("Menor de idade!")
        contadorMenorIdade += 1
    elif idade >= 18:
        print ("Maior de idade!")
        contadorMaiorIdade += 1
print ("\033[34m{}\033[m são/é maiores de idade, \033[34m{}\033[m são/é menores de idade.".format(contadorMaiorIdade,contadorMenorIdade))