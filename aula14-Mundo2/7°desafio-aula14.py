print('SEQUÊNCIA DE FIBONACCI')
numero=int(input('Digite os termos que você deseja mostrar: '))
termo1=0  
termo2=1  
print(f'{termo1} --> {termo2}',end='')
contador=3 #recebe 3 pois ja temos os valores do termo1 e do termo2
while contador<=numero:
    termo3=termo1+termo2 #Cada termo e a soma dos dois n° anteriores 
    print(f' --> {termo3} ', end='')
    termo1=termo2
    termo2=termo3
    contador+=1
print('Fim')