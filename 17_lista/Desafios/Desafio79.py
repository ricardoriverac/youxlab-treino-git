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
            print(f"Sua lista e {lista}")
            