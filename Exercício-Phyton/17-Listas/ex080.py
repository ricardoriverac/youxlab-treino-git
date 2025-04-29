lista = list()
for c in range(5):
    Valor = int(input("Digite o numero: "))
    if c == 0 or Valor > lista[-1]:
        lista.append(Valor)
    else:
        for pos, x in enumerate(lista):
            if Valor <= x:
                lista.insert(pos, Valor)
                break
print(lista)