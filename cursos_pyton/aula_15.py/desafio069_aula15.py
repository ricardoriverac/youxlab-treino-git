addIdade = addMasc = addFemin= 0

while True:
    idade= int(input("Qual a sua idade: \n"))
    if idade >= 18:
        addIdade += 1
    sexo = str(input("Digite o seu sexo: [M/F] \n")).strip().upper()[0]
    if sexo == "M":
        addMasc += 1
    elif sexo == "F":
        if idade < 20:
            addFemin+= 1
    choice = str(input("Continuar? [S/N] \n")).strip().upper()[0]
    if choice == "N":
        print(f"\033[31mPessoas com mais de 18\033[0m: {addIdade}.")
        print(f"\033[38;5;208mHomens cadastrados\033[0m: {addMasc}")
        print(f"\033[33mMulheres com menos de 20 anos\033[0m: {addFemin}")
    print("\n") 
    import datetime


    def sucesso():
        agora = datetime.datetime.now().strftime("%H:%M:%S")
        mensagem = f" Programa finalizado às {agora} ✔️ "
        borda = "═" * len(mensagem)
        
        print("\033[1;32m╔" + borda + "╗")
        print("║" + mensagem + " ║")
        print("╚" + borda + "╝\033[0m")
 # Chamada da função
    sucesso()
    print("\n") 
    break

            
