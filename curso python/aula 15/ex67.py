contador = 0
while True:
    contador = 0
    print ("\t__" * 10)
    numero = int (input("Digite um número para ver sua tabuada: "))
    print ("\t__" * 10)
    while  contador < 10:
            contador += 1
            print (f"\033[34m{numero}\033[m x \033[34m{contador}\033[m = \033[32m{contador*numero}\033[m")
    if numero < 0: 
        print ("Você digitou um número negativo, bye")
        break
print ("Você saiu do programa!!")