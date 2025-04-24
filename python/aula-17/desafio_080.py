lista = list()
for c in range(5):
    n = int(input("Digite o numero: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        for pos, x in enumerate(lista):
            if n <= x:
                lista.insert(pos, n)
                break
print(lista)