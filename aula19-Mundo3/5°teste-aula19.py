estados={}
brasil=[]
for contador in range (0,3):
    estados['estado']=str(input('Digite um estado: '))
    estados['sigla']=str(input('Digite a sua sigla: '))
    brasil.append(estados.copy()) #.copy() --> copia o conteúdo para entrar na lista brasil
for estado in brasil:  #para cada estado na lisa brasil 
    for key, value in estados.items():
        print(f'A chave {key} tem valor {value}')
for estado in brasil:
    for value in estados.values():
        print(value)


