#FUNÇÕES PARA SORTEAR E SOMAR
from random import randint
lista=[]
def sorteio(lista):
    print(f'Sorteando 5 valores da lista {lista} PRONTO!')

for contador in range(5):
    valores= randint(1,11)
    lista.append(valores)

def par(lista):
    soma=0
    for numero in lista:
        if numero%2==0:
            soma+=numero
    print(f'Somando os valores pares de {lista}, temos {soma}')

def main():
    sorteio(lista)
    par(lista)
main()