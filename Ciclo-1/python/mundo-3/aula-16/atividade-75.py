valores = (
    int(input("Digite o 1º valor: ")),
    int(input("Digite o 2º valor: ")),
    int(input("Digite o 3º valor: ")),
    int(input("Digite o 4º valor: "))
)

print(f"\nVocê digitou os valores: {valores}")


quantidade_nove = valores.count(9)
print(f"A) O valor 9 apareceu {quantidade_nove} vez(es).")


if 3 in valores:
    posicao_tres = valores.index(3) + 1  
    print(f"B) O primeiro valor 3 foi digitado na {posicao_tres}ª posição.")
else:
    print("B) O valor 3 não foi digitado nenhuma vez.")


pares = [num for num in valores if num % 2 == 0]
print(f"C) Os números pares digitados foram: {pares if pares else 'Nenhum'}")
