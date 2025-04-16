lista = [ ]
pares = 0

for numeros in range (1,5):
    numerosDigitados = int(input(f'Digite o {numeros}° número: '))
    lista.append(numerosDigitados)
    if numerosDigitados %2 ==0:
     pares += 1

if 3 in lista:
    posicaoTres = lista.index(3)
    print(f'Entre as posiçoẽs 0, 1, 2 e 3, o primeiro número 3 digitado está na posição: {posicaoTres}.')
else:
    print('Não tem número 3 na lista.')

quantosNove = lista.count(9)
print(f'Sua lista tem {quantosNove} números nove.')
print (f'A quantidade de números pares da lista é {pares}.')