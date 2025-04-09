# Faça um programa que tenha uma lista chamada números e duas funções chamada sorteia() e somaPar()
# A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar
# A soma entre todos os valores pares sorteados pela função anterior

from random import randint

todosNumeros = list()

def ql():
    print("\n")

def cabecalho(texto):
    largura = len(texto) + 4
    print("~" * largura)
    print(f"{texto.center(largura)}")
    print("~" * largura)

print("\n")
cabecalho("Sorteando 5 números:")
print(f"   Números sorteados:")

def sorteia(lista):
    for _ in range(5):
        randomNum = randint(1, 10)
        lista.append(randomNum)
        print(randomNum, end=" ")
    print()

ql()
sorteia(todosNumeros)
ql()

cabecalho("Somando os números pares:")

def somarPar(lista):
    soma = sum(num for num in lista if num % 2 == 0)
    print(f"A soma dos números pares é {soma}")

ql()
somarPar(todosNumeros)
ql()