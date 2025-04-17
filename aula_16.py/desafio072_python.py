extensos = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito",
    "nove", "dez", "onze", "doze", "treze", "catorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    numero = int(input("Digite um número de 0 a 20: \n"))
    if numero>= 0 and numero <= 20:
        print(f"Você digitou:{extensos[numero]}.")
        break
    else:
        print("Este número não é válido.", end=" ")