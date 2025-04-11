parentesesAbrindo = []
parentesesFechado = []

expressao = input('Digite uma expressão numérica: ')

for p in expressao:
    if p == '(':
        parentesesAbrindo.append(p)
    else:
        if p == ')':
            parentesesFechado.append(p)

if len(parentesesAbrindo) == len(parentesesFechado):
    print('A expressão está correta!')
else:
    print('A expressão está errada!')
