numero = int(input('Digite um número e descubra se ele é um número primo:'))
isPrime = True
current = (numero // 2)
for i in range(current, 0, -1):
    if numero % i == 0 and i != 1:
        isPrime = False
if isPrime:
    print("O número {} é primo.".format(numero))
else:
    print("O número {} não é primo.".format(numero))