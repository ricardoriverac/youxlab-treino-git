def maior(*valores):
    if len(valores) == 0:
        print("Nenhum valor foi fornecido!")
        return
    maior_valor = max(valores)
    print(f"O maior valor é: {maior_valor}")
print("Exemplo 1:")
maior(10, 20, 30, 40, 50)
print("\nExemplo 2:")
maior(5, 3, 8, 1) 
print("\nExemplo 3:")
maior()