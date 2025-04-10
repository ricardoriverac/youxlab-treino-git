lista=[]

continuar=0
while continuar!='N':
    numeros=int(input("Digite um numero: "))
    lista.append(numeros)
    lista.sort(reverse=True)
    quantLista=len(lista)

    continuar=input("Quer continuar? [S/N] ").strip().upper()

    if continuar=="N":
        if 5 in lista:
            print ("Você digitou",quantLista,"elementos.")
            print("Os valores em ordem descrecente são",lista)
            print ("5 na lista")

        else:
            print ("Você digitou",quantLista,"elementos.")
            print("Os valores em ordem descrecente são",lista)
            print ("5 não está na lista")
