numero = int(input('Digite um número inteiro qualquer para mostrar sua tabuada: '))
for tabuada in range(1, 11):
    resultado = numero * tabuada
    #if resultado % 2 == 0:
        #print (f'\033[1;36mOs resultados pares são {resultado}\033[m ')
    print (f'{numero} x {tabuada} = {resultado} ')