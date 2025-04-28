#definindo um comando pra somar valores
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print(s)

#Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)

#empacotando 
def contador(* num): # o * serva pra q ele possa receber vários valores
    print(num) # mostra em tupla e ai ele aceita tudo q a tupla permite
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números') # mostrando a quantidade de números e deixando mais bonito

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

#empacotando com lista
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

#desempacotando
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)