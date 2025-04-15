# Lista ordenada sem repetições
lista = []
numero = int(input('digite um número: '))
while True:
    valor = int(input("Digite um número: "))
    if valor not in lista:
        lista.append(valor)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não vou adicionar.")

    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar != 'S':
        break
print("\nValores únicos digitados em ordem crescente:")
print(sorted(lista))
print('encerrando o programa... ')