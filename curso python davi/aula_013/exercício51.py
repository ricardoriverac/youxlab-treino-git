pr = int(input('primeiro termo '))
rz = int(input('razão: '))
dc = pr + (10 - 1) * rz
for c in range(pr,dc,rz,rz):
    print('{}'.format(c),end= '>')
print('acabou')