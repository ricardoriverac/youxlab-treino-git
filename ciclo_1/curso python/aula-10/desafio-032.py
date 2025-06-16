#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite um ano:'))
b = ano % 4
print (b)
if b ==0:
    print('O ano de {} é um ano bissexto!'.format(ano))
else:
    print('O ano {} não é um ano bissexto'.format(ano))