print("\033[38;5;213m★" * 40)
lista = []
for c in range(0, 5):
    numero = int(input("\033[38;5;177mDigite um valor: "))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos += 1
print("\033[38;5;177mA lista ordenada é:", lista)
print("\033[38;5;213m★" * 40)