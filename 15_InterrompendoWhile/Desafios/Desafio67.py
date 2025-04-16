import time

while True:
    numero = int(input("Digite um número para ver sua tabuada: "))
    
    print(f"{numero} x 1 = {numero * 1}")
    print(f"{numero} x 2 = {numero * 2}")
    print(f"{numero} x 3 = {numero * 3}")
    print(f"{numero} x 4 = {numero * 4}")
    print(f"{numero} x 5 = {numero * 5}")
    print(f"{numero} x 6 = {numero * 6}")
    print(f"{numero} x 7 = {numero * 7}")
    print(f"{numero} x 8 = {numero * 8}")
    print(f"{numero} x 9 = {numero * 9}")
    print(f"{numero} x 10 = {numero * 10}")
    
   
    while True:
        opcao = input("Deseja continuar? [S/N]: ").strip().upper()
        if opcao == "S":
            print("Você escolheu continuar.\n")
            break
        elif opcao == "N":
            print("Você escolheu encerrar o programa.")
            print("Encerrando programa, aguarde...")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Programa encerrado com sucesso!")
            exit()
        else:
            print("Dados inválidos. Tente novamente.")