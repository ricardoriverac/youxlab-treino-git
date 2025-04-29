lista = []
while True:
    lista.append(int(input("Digite um numero: ")))
    while True:
        escolha = str(input("Deseja continuar?[S/N]: ")).upper().strip()
        if escolha != "S" and escolha != "N":
            print("Erro dados invalidos:tente novamente ")
        if escolha == "S":
            break 
        else:
            lista_ordenada = sorted(lista, reverse= True)
            print(f"Sua lista e {lista}")
            print(f"em ordem decrescente sao {lista_ordenada}")
            if 5 in lista:
                print("O valor 5 faz parte da lista!")
            else:
                print("O o valor 5 nao esta na lista!")
            exit()
            