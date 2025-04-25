#faça um programa que calcule a soma entre todos os numeros impares que
#São multiplos de tres e que se encontram no intervalo de 1 até 500
soma = 0
for c in range(0, 501, 2):
    if c % 3 == 0:
        soma += c
print('A soma dos numeros impares nesse range é{}'.format(soma))       
    
    
    

