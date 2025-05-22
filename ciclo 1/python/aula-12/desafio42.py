print('Analisador de triângulos 2.0:')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos digitados podem formar um triângulo: ', end='')
    if a == b == c:
        print('Equilátero')
    elif a != b != c != a:
        print('Escaléno')
    else:
        print('Isóceles')
else:
    print('Os segmentos digitados não podem formar um triângulo!')