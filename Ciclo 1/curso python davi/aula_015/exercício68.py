from random import randint
while True:
    valor=eval(input("digite o valor:"))
    computador=randint(0,11)
    soma=valor+computador
    usuario=str(input("par ou impar? ")).lower()
    print("voce jogou {} e a máquina {} e a soma é {}".format(valor,computador,soma))
    if usuario=="par":
        if soma%2==0:
            resp="voce ganhou"
        else:
            resp="voce perdeu"
        print(resp)
        if resp=="voce perdeu":
            break
    elif usuario=="impar":
        if soma%3==0:
            resp="voce ganhou"
        else:
            resp="voce perdeu"
        print(resp)
        if resp=="voce perdeu":
            break