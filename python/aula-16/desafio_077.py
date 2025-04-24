tupla = ('café', 'amora', 'calabreso', 'canela', 'flocos')
vogal = ['a', 'e', 'i', 'o', 'u']
for t in tupla:
    print(f'\nVogais da palavra {t.upper()}: ')
    a = list(t)
    b = tuple(a)
    for r in b:
        if r in vogal:
            print(r,end=' ')