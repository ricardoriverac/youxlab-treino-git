dic = dict()
lista = list()
print('\033[33m=-=\033[m'*30)
for c in range(0,1):
    dic['Nome'] = str(input('Qual o nome do aluno?: '))
    dic['Media'] = float(input('Qual a média do aluno?: '))
    lista.append(dic.copy())
print('\033[33m=-=\033[m'*30)

for k, v in dic.items():
    print(f'- {k} é {v}')

if dic['Media'] > 7:
    print('- Situação é igual a Aprovado')
    
else: 
    print('- Situação é igual a Reprovado')
print()