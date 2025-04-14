numero=int(input('digite um numero inteiro:')) 
termo1=0
termo2=1
print('{}  -> {}'.format(termo1, termo2))
contador=3
while contador<=numero:
    termo3= termo1+termo2
    print('->{}'.format(termo1, termo2))
    termo1 = termo2
    termo2 = termo3
    contador  += 1
print("-> Fim!")