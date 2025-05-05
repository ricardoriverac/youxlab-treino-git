print('--------------------------------------------')
contador = 1 
while True:
    numero = int(input('♡ ♡ ♡ Digite um número e descubra a sua tabuada!!!'))
    if numero < 0:
        break
    for i in range(1,11):
        print(f'{numero} x {i} = {numero * i}')
print('fimm')