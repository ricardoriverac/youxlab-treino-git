def ficha(n='<Desconhecido>',quantidade=0):
    print(f'O jogador {n} fez {quantidade} gols no campeonato!! ')


nome=str(input('Me diga o nome do jogador: '))
gols=int(input('Quantidade de gols: '))

if gols.isnumeric():
    gols = int(gols)

else:
    gols = 0

if nome.strip() == '':
    ficha(quantidade=gols)


else:
    ficha(nome,gols)







    


