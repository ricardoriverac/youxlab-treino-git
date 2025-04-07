numero = int(input("Digite um número: "))
contador = 0
for c in range(1, numero +1):
    if numero % c == 0:
        print("\033[32m", end=" ")
        contador = contador + 1
    else:
        print("\033[34m", end=" ")
    print('{}'.format(c), end=" ")
print("\n\033[mO número {} foi divisivel {} vezes".format(numero, contador))
if contador == 2:
    print("Ele é PRIMO!")
else:
    print("não é PRIMO!") 