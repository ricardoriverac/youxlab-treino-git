# * ele faz o valor ser uma tupla que pode receber varios valores 'Parámetros'
def somavalor(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos valores {valores} somados foram {s}')


#programa principal
somavalor(2,1)
somavalor(9,1,2,3)
somavalor(3,10,4,50,10,2)