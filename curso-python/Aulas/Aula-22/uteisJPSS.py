def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

def par(n):
    if n % 2 == 0:
        print("O seu número é par.")

def impar(n):
    if n % 2 != 0:
        print("O seu número é impar.")

def parOuImpar(n):
    if n % 2 == 0:
        print("O seu número é par.")
    else:
        print("O seu número é impar.")

def cabecalho(texto):
    largura = len(texto) + 8
    print("~" * largura)
    print(f"{texto.center(largura)}")
    print("~" * largura)

def ql():
    print("\n")