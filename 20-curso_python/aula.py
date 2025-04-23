def soma(a, b):
    s = a + b
    print(s)


soma(3, 6)
soma(5, 2)
soma(87, 4)

def contador(*num):
    numeros = len(num)
    print(f'Recebi os números {num} que no total são {numeros} números. ')

contador(1, 8, 43, 5)
contador(7, 4, 2)

def cont(*num):
    for valor in num:
        print(f'{valor}', end=' ')
    print('FIMM!')

cont(3, 6, 4, 15)


valores = [2, 5, 8, 9, 0]
def dobra(lista):
    pos = 0
    while pos < len(valores):
        lista[pos] *= 2
        pos+=1

dobra(valores)
print(valores)

def soma2(*num):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos valores {valores} é {s}')
    
soma2(2, 5, 9 ,3)

