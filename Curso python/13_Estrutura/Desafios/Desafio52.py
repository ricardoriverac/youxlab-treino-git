numero=int(input("Digite um numero: "))
for c  in range(1,numero +1):
    if numero % c == 0:
        print(f"{[c]}")
    elif numero % c == 2:
        print(f"{(c)}")