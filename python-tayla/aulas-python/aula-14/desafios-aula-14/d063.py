numero = int(input('Digite um número inteiro: '))
posicao = numero

# #variaveis pra dar o valor inicial da sequencia
a = 0
b = 1

#inicia o contador pra contole de quantas vezes o while vai rodar
contador = 0

while contador < posicao:
    print(f'{a} ->', end=' ')
    a, b = b, a + b
    contador += 1
print()
print(f'Esses são os {numero} primeiros termos da sequência de Fibonacci')