pessoas={'Nome':'Gustavo','Sexo':'M', 'Idade': '17'}
pessoas['Nome'] = 'VITORIA'
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k , v in pessoas.items():
    print(f'{k}, {v}')
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
#del pessoas['Sexo']#Apaga
