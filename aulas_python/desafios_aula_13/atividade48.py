print('\033[1;34m-=-=-=-=-= Bem vindo(a)! =-=-=-=-=-\033[m')
n1 = int(input('Digite um número que irei ver os divisiveis por 3 e depois somar todos: '))
zero = 0
contador = 0
for c in range(1, n1, 2):
    if c % 3 == 0:
        contador = contador +1
        zero = zero +c
        
print('A soma de todos os números impares de 0 a 500 que são divididos por 3 é: {}\nE os números divisiveis são {}'.format(zero, contador))
    