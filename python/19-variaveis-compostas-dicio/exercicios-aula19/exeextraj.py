info = dict()
lista = list()
for c in range(0,6):
    palavra = input('Palavra: ')
    lista.append(palavra)
for l in lista:
    if l in info:
        info[l] += 1
    else:
        info[l] = 1
print(info)