#Crie um programa que tenha uma tupla com varias palavras (não usar acentos).
#Depois disso, voce devera mostrar, para cada palavra, quais são as suas vogais.

palavras = ("escola", "casa", "abaixo", "assento", "esquadrilha", "")

for p in palavras:
    print(f"\nNa palavra {p.upper()} temos:", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")