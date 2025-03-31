#Faça um programa que leia tres numeros e mostre qual deles é o maior e qual deles é o menor

num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
num3 = int(input('Digite mais um número:'))

if num1 <= num2:
    print('o Número {} é o menor'.format(num1))
if num2 <= num1:
    print('O número {} é o maior'.format(num1))
if num3 <= num1:
    print('O número {} é o menor'.format(num3))
if num3 <= num2:
    print('O número {} é o menor'.format(num3))
