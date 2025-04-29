import random
iten = ("PEDRA","PAPEL","TESOURA")
pc = random.randint(0,2)
escolha= int(input("Numero 0 para [PEDRA]...Numero 1 para [PAPEL]...Numero 2 para [TESOURA]... Digite sua escolha: "))
print("O computador escolheu ,{}".format(iten[pc]))
print("Voce escolheu {}".format(iten[escolha]))
if pc == escolha:
    print("EMPATE")
elif (escolha == 0 and pc == 1)or(escolha == 1 and pc == 2 ) or (escolha == 2 and pc == 0):
    print("VOCE PERDEU")
else:
    print("VOCE GANHOU")

