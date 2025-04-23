lista = [[],[]]
numero = 0
for c in range (7):
    numero = int (input(f"Digite o { c + 1}º número : "))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
lista[0].sort()
lista[1].sort()
print (f"\tA lista completa é {lista}")
print (f"\tA lista de números pares é {lista[0]}")
print (f"\tA lista de números ímpares é {lista[1]}")

