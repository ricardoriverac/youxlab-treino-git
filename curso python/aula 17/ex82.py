continuacao = 'S'
lista = []
listapar = []
listaimpar = []
while continuacao == "S":
    numero = int (input ("Digite um número: "))
    lista.append(numero)
    continuacao = str (input ("Quer continuar [S/N] ? ")).strip().upper()
    if numero % 2 == 0:
        listapar.append(numero)
    else:
        listaimpar.append(numero)
print (f"\tA lista completa é {lista}")
print (f"\tA lista de números pares é {listapar}")
print (f"\tA lista de números ímpares é {listaimpar}")

