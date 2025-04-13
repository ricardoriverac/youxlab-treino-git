def linha(tam=42):
    return "-" * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    for i, item in enumerate(lista, 1):
        print(f"{i} - {item}")
    print(linha())

    while True:
        try:
            opc = int(input("Sua opção: "))
            if 1 <= opc <= len(lista):
                return opc
            else:
                print("Erro! Digite uma opção válida.")
        except ValueError:
            print("Erro! Digite um número inteiro válido.")
