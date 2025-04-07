soma = 0
cont = 0
for c in range(1, 7):
    numeros = int(input(f"Digite {c} valor:"))
    if numeros % 2 == 0:
        soma+=numeros
        cont += 1
print(f"Você digitou {cont} números PARES e a soma total deles foi {soma}")