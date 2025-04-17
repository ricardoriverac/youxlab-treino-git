import time
total = totmil= menor= cont =0
while True:
    print("=-=-=-=-"*2)
    print("   LOJA TOP ")
    print("=-=-=-=-"*2)
    nome =str(input("Digite o nome do produto: "))
    preço = int(input("Qual preço R$: "))
    cont += 1
    total += preço
    if preço >1000:
        totmil += 1
    if cont == 1:
        menor= preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    resp =""
    while True:
        escolha = str(input("Deseja continuar? [S][N]: ")).upper()[0].strip()
        if escolha == "S":
            print("=-=-=-=-=-=-=-=-=-=-=-")
            print("Voce selecionou continuar")
            print("=-=-=-=-=-=-=-=-=-=-=-")
            print("Carregando", end="") 
            for _ in range(5):
                time.sleep(1)  
                print(".", end="", flush=True)
            print("")
            break
        if escolha != "S"and escolha != "N":
            print("Dados invalidos tente novamente: ")
            for _ in range(5):
                time.sleep(1)
                print(".", end="", flush=True)
        if escolha  == "N": 
            print("Carregando", end="")
            for _ in range(5):
                time.sleep(1)
                print(".", end="", flush=True)
            
            print("Fim do programa")
            print(f"O total da compra  foi R${total}")
            print(f"Temos {totmil} produtos custando mais de R$1000.00")
            print(f"O produto mais barato foi {barato} que custa R${menor}")
            exit()
                
            
        
        
            
     
