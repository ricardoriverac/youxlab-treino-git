def soma(a, b):
     s = a + b 
     print(f'A = {a} e B = {b}')
     print(f'A soma de A e B = {s}')

# Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)

def contador(* núm):
    # for valor in núm:
    #     print(f'{valor}', end=' ')
    # print('FIM!')
    tam = len(núm)
    print(f'Recebi os valores {núm} e são {tam} números ')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos+=1


lista = [6, 3, 9, 1, 0, 2]
dobra(lista)
print(lista)