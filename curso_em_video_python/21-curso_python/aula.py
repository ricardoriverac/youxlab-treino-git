def soma(a=0, b=0, c=0):
    """""
    --> Faz a soma de três valores e mostra o resultado na tela.
    a: primeiro valor
    b: segundo valor
    c: o terceiro valor
    """""
    s = a + b + c
    print(f'A soma vale {s}.')

soma(4, 6, 2)
soma(2, 9) #deu erro então eu coloquei o 0 depois do c, ai quando não coloca nada no terceiro valor ele vale 0
soma(6, 9)

def teste(b):
    b += 4
    c = 6
    print(f'O a dentro do teste vale {a}')
    print(f'O b dentro do teste vale {b}')
    print(f'O c dentro do teste vale {c}')
#PROGRAMA PRINCIPAL
a = 8
teste(f'O a fora vale {a}')
