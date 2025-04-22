dic = {}
notas_lista = []
cont = 0
sit = ''

def notas(dic,cont,sit):
    """
    -> Função para analisar a nota de vários alunos.
    :param dic: dicionário que será prenchido com as informações.
    :param cont: contador de alunos.
    """
    while True:
        notas = float(input(f'Nota {cont + 1} (999 para parar): '))
        if notas == 999:
            break
        cont += 1
        notas_lista.append(notas)
        
    media = sum(notas_lista) / len(notas_lista)

    if media >= 6:
        sit = 'BOA'
    else:
        sit = 'RUIM'
    if notas_lista:
        dic["Quantidade de notas"] = len(notas_lista)
        dic["Maior nota foi"] = max(notas_lista)
        dic["Menor nota foi"] = min(notas_lista)
        dic["A média das notas foi"] = media
        dic["A situação é"] = sit        
    else:
        dic["Maior nota foi"] = "Nenhuma nota registrada"
        dic["Menor nota foi"] = "Nenhuma nota registrada"
        dic["A média das notas foi"] = "Nenhuma nota registrada"

    print('--'*35)
    for k,v in dic.items():
        print(f'{k}: {v}')
    print('--'*35)
    
notas(dic,cont,sit)
help(notas)
