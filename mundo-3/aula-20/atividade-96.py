def area():
    try:
        comprimento = float(input('Comprimento (em metros): '))
        largura = float(input('Largura (em metros): '))
        a = comprimento * largura
        print(f'A área do terreno é de {a:.2f} m²')
    except ValueError:
        print("Por favor, insira apenas números válidos.")

area()
