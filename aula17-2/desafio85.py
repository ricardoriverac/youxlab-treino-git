lista = list()
par = list()
impar = list()
for c in range(1,8):
    num = int(input(f'Digite o {c} valor:'))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print('=-'*14)
print(f'Voce digitou os valores {sorted(lista)}')
print(f'Os valores pares digitados são {sorted(par)}')
print(f'Os valores impares digitado são {sorted(impar)}')
