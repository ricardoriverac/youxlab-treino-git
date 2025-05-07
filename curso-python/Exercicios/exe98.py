# Faça um programa que tenha uma função chamada contador() - 
# que recebe três paramentros: inicio, fim e passo e realize a contagem.

# Seu programa tem que realizar tres contagens atraves da função criada:

# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada.

def cabecalho(texto):
    largura = len(texto) + 8
    print("\n")
    print("~" * largura)
    print(f"{texto.center(largura)}")
    print("~" * largura)
    print("\n")

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ')
    print()


cabecalho("Contagem de 1 até 10 de 1 em 1:")
contador(1, 10, 1)

cabecalho("Contagem de 10 até 0 de 2 em 2:")
contador(10, 0, 2)
print("\n")

print('Agora é sua vez de personalizar:')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

cabecalho(f"Contagem de {i} até {f} de {p} em {p}:")
contador(i, f, p)
