numeros = 0
numeros1 = int(input('Digite um número: '))
print('OBSERVAÇÃO: digite 999 quando quiser parar.')
lista = [ ]
quant = 0
a = 999
while numeros != 999:
    numeros = int(input('Digite outro número: '))
    quant +=1
    lista.append(numeros)
    conta = sum(lista)
    conta2 = conta + numeros1 - a
    media = conta2/quant
    maior = max(lista)
    menor = min(lista)
print('A média dos números que você digitou foi: {:.2f}'.format(media))
print('O menor número entre eles foi {}, e o maior foi {}'.format(menor, maior))