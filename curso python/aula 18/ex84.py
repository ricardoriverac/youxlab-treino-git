pessoas = []
dados = []
continuacao = "S"
maior = 0
menor = 0
while continuacao == "S":
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Peso: ")))
    pessoas.append(dados[:])
    print(dados)
    continuacao = str (input ("Quer continuar [S/N] ? ")).strip().upper()
    if dados[1] > maior:
        maior = dados [1]
    if dados[1] < menor:
        menor = dados[1]
    #pessoas.append(dados[:])
    dados.clear ()
print (f"Quantas pessoas foram cadastradas {len(pessoas)}")
print (pessoas)
print (f" O maior peso foi de : {maior}kg.")   
print (f" O menor peso foi de : {menor}kg.")   
