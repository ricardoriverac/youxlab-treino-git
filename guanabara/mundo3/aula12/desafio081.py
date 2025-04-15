numeros = []

while True:
    try:
        num = int(input("Digite um número: "))
        if num not in numeros:
            numeros.append(num)
            print("Número adicionado com sucesso!")
        else:
            print("Número já está na lista, não será adicionado.")
    except ValueError:
        print("Por favor, digite um número válido.")
    
    continuar = input("Deseja continuar? [S/N]: ").strip().upper()
    if continuar != 'S':
        break

if 5 in numeros:
    print("O número 5 está presente.")
else:
    print("O número 5 não está presente.")

print("\nNúmeros digitados (sem repetição), em ordem decrescente:")
numeros.sort(reverse=True)
print(numeros)
