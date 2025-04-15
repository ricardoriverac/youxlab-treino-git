while True:
    numero = int(input("Digite um número para ver a tabuada (negativo para sair): "))
    
    if numero < 0:
        print("Programa encerrado. Até mais!")
        break

    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print("-" * 30)
