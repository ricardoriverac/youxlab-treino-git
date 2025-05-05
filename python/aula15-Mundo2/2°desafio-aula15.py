#TABUADA 3.0
while True:
    numero=int(input('Digite um n° para ver sua tabuada: '))
    if numero<0:  #se numero menor que 0 (negativo)
        break     #acaba
    for contador in range(1,11):
        print(f'{numero}x{contador}={numero*contador}')
print('ERRO, não é permitido números negativos!')