lista = []
for c in range(0,5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print("Adicionado ao final da lista")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                prnt(f"Adicionado na posiçao {pos}")
                break
            pos = + 1
print("======"*8)
print(f"os valores digitados em ordem foram {lista}")