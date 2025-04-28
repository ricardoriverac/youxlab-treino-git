numero = int(input('Digite três números: '))
numero2 = int(input(' '))
numero3 = int(input(' '))
escolha = numero, numero2, numero3
menorNumero = min(escolha)
maiorNumero = max(escolha)

print('Entre {}, o menor número é: {}'.format(escolha, menorNumero))
print('Entre {}, o maior número é: {}'.format(escolha, maiorNumero))