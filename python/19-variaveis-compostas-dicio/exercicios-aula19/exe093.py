gols = list()
campo = {
    'nome' : str(input('Nome do jogador: ')),
    'partidas' : int(input('Quantas partidas ele jogou: '))
}
for p in range(campo['partidas']):
    gols.append(int(input(f'Quantos gols na {p+1}°: ')))
campo['gols'] = gols[:]
#"sum" soma todos os valores em uma lista
campo['total'] = sum(gols)
print('-='*30)
print(campo)
print('-='*30)
for k , v in campo.items():
    print(f'{k} tem o valor {v} ')
print('-='*30)
print(f'O jogador {campo["nome"]} jogou {campo["partidas"]} partidas')
for c in range(campo['partidas']):
    print(f'-Na partida {p} , ele fez ', end='' )
    print(campo['gols'][c])
totaldegols = campo['total']
print(f'No total deu {totaldegols} gols ')


