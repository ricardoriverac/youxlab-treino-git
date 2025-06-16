#Faça um programa que leia um número inteiro e mostre se ele é par ou impar

num = int(input('Digite um número inteiro:'))
result = num % 2
if result == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é IMPAR'.format(num))
