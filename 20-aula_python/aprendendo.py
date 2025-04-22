def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
    
def bonito():
    print('='*30)

#programa pricipal
titulo(' Cruziero maior de Minas')
titulo('Bi-Libertadores')
titulo('Hexa Copa do Brasil')


def soma(a, b):
    bonito()
    print(f'A soma de A = {a} e B = {b}')
    bonito()
    s = a + b
    bonito()
    print(f'A soma de A + B = {s}')
    bonito()

#programa pricipal
soma(b=4, a=5)
soma(5, 5)


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} número')
    #print(num)
    #for valor in num:
        #print(valor)
        #print(f'{valor} ', end='')
    #print('FIMM!!!')


contador(2, 4, 5)
contador(4, 7, 8)
contador(2, 3)


def dobra(lst):
    pos = 0
    while pos <len(lst):
        lst[pos] *=2
        pos += 1

valores = [6, 12, 45, 1]
dobra(valores)
print(valores)


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(0, 3)
soma(4, 2, 3)