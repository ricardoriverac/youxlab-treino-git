primeiroNumero = int(input('Digite um número: '))
segundoNumero = int(input('Digite outro número: '))
terceiroNumero = int(input('Digite mais um número: '))
quartoNumero = int(input('Digite o último número: '))
numeros = primeiroNumero, segundoNumero, terceiroNumero, quartoNumero
tuplaNumeros = tuple(numeros)
valorNove = tuplaNumeros.count(9)

print(f'Você digitou os valores {tuplaNumeros}')
print(f'O \033[35mVALOR 9\033[m apareceu {valorNove} vezes ')

if primeiroNumero != 3 and segundoNumero != 3 and terceiroNumero != 3 and quartoNumero != 3:
    print('O número 3 não apareceu em nenhuma posição ')
else:
    posicaoTres = tuplaNumeros.index(3)
    print(f'O \033[35mNÚMERO 3\033[m apareceu na posição {posicaoTres+1}')

print('Os \033[35mVALORES PARES\033[m digitados foram ', end='')
for num in tuplaNumeros:
    if num % 2 == 0:
        print(num, end=' ')  
print ('')



    