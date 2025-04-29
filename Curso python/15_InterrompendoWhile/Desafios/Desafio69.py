import time
tot18 = toth = totm20 = 0
while True:
    print("=-=-=" * 4)
    print("CADASTRE UMA PESSOA")
    print("=-=-=" * 4)
    idade = int(input("Idade: "))
    sexo = " "
    while True:
        print("=-=-=" * 4)
        sexo = str(input("Sexo: [M/F] ")).upper()[0].strip()
    
        if idade >= 18:
            tot18 += 1    
        if sexo == "F" and idade <20:
            totm20 =+ 1
        if sexo == "M" and idade >18:
            tot18 += 1  
        print("=-=-=" * 8)
        if sexo != "M" and sexo != "F":
            print("Dados invalidos tente novamente")
            print("=-=-=" * 8)
        else:
            break
    while True:
        opçao = str(input("Deseja continuar:[S/N] ")).upper()[0].strip() 
        print("=-=-=" * 4)  
        if opçao == "S":
            print("=-=-=" * 4)
            print("Iniciando novamente aguarde...")
            print(".")
            time.sleep(0.5)
            print("..")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            break
        elif opçao == "N":
            print("Encerrando...")
            print(".")
            time.sleep(0.5)
            print("..")
            time.sleep(0.5)
            print("...")
            print("Gerando estatisticas...")
            print(".")
            time.sleep(0.5)
            print("..")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            print(f"o total de mulhres abaixo de 20 anos de idade foi: [{totm20}]")
            print(f"Total de homens acima de 18 anos foi [{tot18}]")
            print("Encerrado com sucesso!!")
            exit()
        else:
            print("Dados invalidos tente novamente")
