valores = tuple(int(input('Digite valores '))for c in range(1, 5))
print(f"\nVocê digitou os valores: {valores}")


quantidade_nove = valores.count(9)
print(f"O valor 9 apareceu {quantidade_nove} vez(es).")


if 3 in valores:
    posicao_tres = valores.index(3) + 1  
    print(f"O primeiro valor 3 foi digitado na {posicao_tres}ª posição.")
else:
    print("O valor 3 não foi digitado nenhuma vez.")


pares = [num for num in valores if num % 2 == 0]
print(f"Os números pares digitados foram: {pares if pares else 'Nenhum'}")