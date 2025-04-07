import time 
print('\033[1;34m-=-=-=-=-= Cálculo do Fatorial =-=-=-=-=-\033[m')
numero = int(input('Digite um número para eu calcular seu fatorial: '))
resultado = 1
for i in range(1, numero + 1):
    resultado *= i

print(f'Calculando {numero}... ')
time.sleep(2)
print(F'O número {numero} fatoriado é: {resultado} ')