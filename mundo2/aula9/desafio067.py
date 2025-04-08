while True:
    numero = int(input("gostaria de saber a tabuada de qual número? "))
    if numero < 0:
        break
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")