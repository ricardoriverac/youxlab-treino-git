# Este arquivo serve para eu testar meus códigos e observar como eles se comportam,
# sem precisar escrever um código gigante.

# def dobra(lista):
#     pos = 0
#     while pos < len(lista):
#         lista[pos] *= 2
#         pos += 1

# valores = [5, 2, 5, 1, 1, 6]
# dobra(valores)
# print(f"Valores dobrados:", valores)

def soma1(* valores):
    s = 0
    for numero in valores:
        s += numero
    print(f"\nSomando os valores {valores} temos {s}.\n")

soma1(5, 2)
soma1(2, 4)

def lin():
    print("-=-" * 10)

def soma(texto, a, b):
    lin()
    print(texto.center(25))
    lin()
    print(f"\nValor A = {a}")
    print(f"Valro B = {b}")
    s = a + b
    print(f"A soma de A + B = {s}\n")

soma("Continha1", 1, 5)
soma("Continha2", 2, 3)

def contador(* numero):
    for valor in numero:
        print("Valor do contador:", valor)

contador(4, 5, 6)
contador(2, 1, 1)