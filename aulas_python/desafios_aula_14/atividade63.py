import time
print('\033[1;34m-=-=-=-=-= Sequência de Fibonacci v1.0 =-=-=-=-=-\033[m')
time.sleep(1)

primeiroNum = 0
segundoNum = 1
cont = 0
termos = int(input('Quantos termos você quer mostrar? '))

while cont < termos:
   print(primeiroNum)
   soma = primeiroNum + segundoNum
   primeiroNum = segundoNum
   segundoNum = soma 
   
   cont += 1
   
print('\033[1;34m-=-=-=-=-= Execute novamente para mais! =-=-=-=-=-\033[m')