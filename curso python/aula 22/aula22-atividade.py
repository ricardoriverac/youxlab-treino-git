#   módulos e pacotes
# ModularizaÇão
'''Surgiu no início da década da 60
Sistamas ficando cada vaz maioras
Foco: dividir um programa granda
Foco: aumantar a legibilidade
Foco: facilitar a manutenção
'''
def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

num = int(input("Digite um valor: "))
fat = fatorial(num)
print(f"O fatorial de {num} é {fat}")
# import uteis