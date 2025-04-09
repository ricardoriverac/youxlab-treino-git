numeros = 0
numeros1 = int(input('Digite um número: '))
lista = [ ]
quant = 0
a = 999
while numeros != 999:
    numeros = int(input('Digite outro número: '))
    quant +=1
    lista.append(numeros)
    conta = sum(lista)
    conta2 = conta + numeros1 - a
print('A quantidade de números que você digitou foi: {}'.format(quant + 1))
print('A soma entre eles foi {}'.format(conta2))
