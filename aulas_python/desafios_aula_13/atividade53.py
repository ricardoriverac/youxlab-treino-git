import time

print('\033[1;34m-=-=-=-=-= Bem vindo(a)! =-=-=-=-=-\033[m')
time.sleep(1)

algo = str(input('Digite algo: '))
contrario = algo[::-1]

if contrario == algo:
    print('Esse é um Palíndromo!!')
    
else:
    print('Não é um Palíndromo!!')
    
print('\033[1;34m-=-=-=-=-= FIM! =-=-=-=-=-\033[m')