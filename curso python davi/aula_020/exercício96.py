def área(largura, comprimento):
    return largura * comprimento
largura = float(input("Digite a largura do terreno (em metros): "))
comprimento = float(input("Digite o comprimento do terreno (em metros): "))
area_terreno = área(largura, comprimento)
print(f"A área do terreno é {area_terreno} metros quadrados.")