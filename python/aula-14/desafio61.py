p = int(input('Qual o primeiro termo?  '))
r = int(input('E qual a razão?  '))
c = 1
while c <= 10:
    a = p + (c - 1) * r
    print(a, end='')
    print(' → ' if c < 10 else '. FIM! ', end='')
    c += 1