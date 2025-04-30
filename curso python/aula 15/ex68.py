from random import randint
print ("\t===" * 20)
print ("VAMOS JOGAR PAR OU ÍMPAR... ")
print ("\t===" * 20)
contadorAcertos = 0
while True:
    computador = randint (0,10)
    jogador = int (input ("Digite um número: "))
    soma = jogador + computador
    escolha = str (input("Você escolhe par ou impar ? [P ou I]")).strip().upper()
    while escolha not in "PI":
        escolha = str (input("Você escolhe par ou impar ? [P ou I]")).strip().upper()
    if soma % 2 == 0:
        print ("PAR")
    else:
        print ("ìmpar")
    print (f"Você jogou {jogador} e o computador jogou {computador}, resultando em {soma}")
    if escolha == "P":
        if soma % 2 == 0:
            print ("Número par, VOCẼ VENCEU!!")
            contadorAcertos += 1
        else:
            print ("VOCÊ PERDEU!!")
            break
        print ("Vamos jogar novamente...")
    elif escolha == "I":
        if soma % 2 == 1:
            print ("Número impar, VOCẼ VENCEU!!")
            contadorAcertos += 1
        else:
            print ("VOCÊ PERDEU!!")
            break
        print ("Vamos jogar novamente...")
print ("FIM DE JOGOOO!!!")
print (f"Quantidade de vitórias: {contadorAcertos}.") 