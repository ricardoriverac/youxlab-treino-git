pesomaior= 0
pesomenor= float("inf")
for pesos in range(0,5):
    peso = float(input(f"Digite o peso da {pesos+1 } pessoa: "))
    if peso > pesomaior:
        pesomaior = peso
    if peso < pesomenor:
        pesomenor = peso
print(f"Maior peso e {pesomaior}")
print(f"Menor peso e {pesomenor}")