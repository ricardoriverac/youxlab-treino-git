resp = "S"
resp = "N"
soma = quant = media = maior = menor=0
while True:
    num = int(input("Digite um número: "))
    soma += num
    quant += 1

    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    while True:
        resp = input("Quer continuar [S/N]: ").strip().upper()
        if resp in ["S", "N"]:
            break
        else:
            print("Erro: dados invlidos Digite apenas 'S' ou 'N':")

    if resp == "N":
        media = soma / quant
        print(f"\nVocee digitou {quant} nnumeros e a media e {media:.2f}")
        print(f"O maior valor foi {maior} e o menor foi {menor}")
        break