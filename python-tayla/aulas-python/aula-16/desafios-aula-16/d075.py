a = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print('-=' * 12)
print(f'O valor nove apareceu {a.count(9)} vezes')
if a.count(3) > 0:
    print(f'O valor 3 apareceu primeiro na {a.index(3)+1}º posição')
else:
    print(f'O valor 3 não apareceu nehuma vez')
print('Os valores pares foram: ', end='')
for x in a:
    if x % 2 == 0:
        print(x, end=' | ')