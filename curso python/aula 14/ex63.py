numero = int (input("Digite um número para ter a sequência de Fibonacci: "))
a = 0
b = 1
contador = 0
while contador < numero:
    print(a)
    a, b = b, a + b
    contador = contador + 1
print ("FIM")