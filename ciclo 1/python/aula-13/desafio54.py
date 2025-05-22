i=2022
ma=0
me=0
for c in range(0,7):
    an=int(input('Ano de nascimento: '))
    if i - an >= 25:
        ma+=1
    if i - an <= 25:
        me+=1
print('{} são de maior e {} são de menor'.format(ma,me))