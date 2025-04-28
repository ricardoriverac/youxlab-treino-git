numero= 0
while True:
    numero= int(input('Digite seu número: '))
    if numero <0:
        break
    
    for multiplicacao in range(0, 11):
            print('{} x {}= {}'.format(numero, multiplicacao , numero * multiplicacao))
    