numeros = []
while True:
    valor = int(input("Digite um número: "))
    if valor not in numeros:
        numeros.append(valor)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não vou adicionar.")
    
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar != 'S':
        break
print("\nVocê digitou os seguintes valores únicos em ordem crescente:")
print(sorted(numeros))