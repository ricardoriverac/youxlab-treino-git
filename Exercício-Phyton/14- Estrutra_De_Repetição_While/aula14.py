#-Pro número se ir de 0 a 10.
#c = 1
#while c < 10:
#    print(c)
#    c = c + 1
#print('Fim')
#--------------------------------
#-Quando escolher o número 0 vai parar.
# n = 1 
#while n != 0:
#    n = int(input('Digite o valor:'))
#---------------------------------------------
#-Enquanto eu estiver apertando sim ou não, dirá se eu poderei continuar comentando números
#r = 'S'
#while r == 'S':
#    n =int(input('Digite um valor:'))
#    r = str(input('Quer continuar? [S/N]')).upper()
#print('Fim') 
#--------------------------------------------------------
#par = impar = 0
#while n != 0:
#    n = int(input('Digite um valor: '))    
#    if n % 2 == 0:
#        par = +1
#    else:  
#        impar += +1

#print(f'Vo ce digitou {par} números pares e {impar} numeros impares!')



#import time 

#numero = int(input('Digite um número para eu calcular seu fatorial: '))

#resultado = 1

#for i in range(1, numero + 1):

#    resultado *= i


#print(f'Calculando {numero}... ')

#time.sleep(2)

#print(F'O número {numero} fatoriado é: {resultado} ')
















numero = int(input('Digite um número inteiro: '))
fatorial = numero
resultado = numero
while fatorial != 1:
    fatorial = fatorial - 1
    resultado = fatorial * resultado
print(f'O fatorial do número {numero} é {resultado} ')