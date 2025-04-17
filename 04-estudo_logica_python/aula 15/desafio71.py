print('--------BANCO---------')
valor=int(input('Qual valor você quer  sacar?'))
total= valor
nota=50
todasnotas=0
while True:
    if total >= nota:
        total -= nota
        todasnotas += 1
    else:
        if todasnotas > 0:
            print(f'Total de {todasnotas} células de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        todasnotas = 0
        if total == 0:
            break
print(('------VOLTE SEMPRE------'))
