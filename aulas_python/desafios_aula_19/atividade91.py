import random
Dic = dict()
listaN = []
listaJ = []
print()
for c in range (1,5):
    escolha = random.randint(0,6)
    listaN.append(escolha)
    print(f'Jogador {c} tirou {escolha} no dado')
Dic['Jogador '] = listaJ
Dic['Números'] = listaN

print('\033[33m=-=\033[m'*30)
print(Dic)
