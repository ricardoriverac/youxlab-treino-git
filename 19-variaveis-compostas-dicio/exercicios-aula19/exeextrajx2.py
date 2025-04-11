#segundo exercicio prospoto pelo jander
total = list()
notas = {
    'Ana': [7,8,9],
    'Bruno' : [5,6,5],
    'Clara': [10,9,10]
}
for v in notas.values():
    total.append(v)
soma = list()
for sublista in total:
    soma.append((sum(sublista)) / 3)
for i in range(len(sublista)):
    if i == 0 :
        notas['Ana'] = soma[0]
    if i == 1 :
        notas['Bruno'] = soma[1]
    if i == 2 :
        notas['Clara'] = soma[2]
for k , v in notas.items():
    print(f'{k}: {v:.1f}')
















# print(total1)