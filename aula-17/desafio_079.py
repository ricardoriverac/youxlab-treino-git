lista = [] #poderia ser lista = lista()
resposta = "S"

while resposta == "S":
    v = int(input("Digite um valor:")) #valor que será add a lista
    if v in lista:
        print("NÚMERO DUPLICADO, valor não será adicionado a lista!")
    else:
        lista.append(v)
    while True: #Loop
        resposta = str(input("Quer continuar?")).upper().strip()
        if resposta not in "SN":
            print("Resposta errada! Tente novamente.")
        elif resposta == "N":
            break
        elif resposta == "S":
            break
print("=-="*20)
lista.sort()
print(f"Sua lista: {lista}")