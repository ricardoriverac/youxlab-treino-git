valores = tuple(int(input('digite numeros aleatórios 4 vezes: '))for c in range(1, 5))
print(f'o numero nove aparece {valores.count(9)} vezes')
print(f'o valor 3 foi digitado pela primeira vez na {valores.index(3)+1}º posição' if 3 in valores else
'não foi digitado valor o 3')
print('valores pares digitados foram', end=' ')
print({n for n in valores if n % 2 == 0}, end=' ')