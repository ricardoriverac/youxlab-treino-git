def linha():
    print("\n")

def cabecalho1(texto):
    largura = len(texto) + 8
    print("~" * largura)
    print(f"{texto.center(largura)}")
    print("~" * largura)

def cabecalho2(texto1, texto2, texto3, texto4, texto5, texto6, texto7):
    largura = len(texto5) + 15
    print("~" * largura)
    print(f"{texto1.center(largura)}")
    print("~" * largura)
    print(f"{texto2.center(largura)}")
    print("~" * largura)
    print(f"{texto3.center(largura)}")
    print("~" * largura)
    print(f"{texto4.center(largura)}")
    print("~" * largura)
    print(f"{texto5.center(largura)}")
    print("~" * largura)
    print(f"{texto6.center(largura)}")
    print("~" * largura)
    print(f"{texto7.center(largura)}")
    print("~" * largura)

# cabecalho2("Menu", "1 - Ver saldo", "2 - Ver limite", "3 - Depositar", "4 - Sacar")

# Anotações/ideias
# menu
# Menu - titulo
# 1 - Ver saldo - opção
# 2 - Ver limite - opção
# 3 - Depositar - opção
# 4 - Sacar - opção