valores= ()
pares=0
for posisao in range(1,5):

    numeros=int(input(f'Digite o {posisao} número: '))
    valores += (numeros, )
#Bom, aqui termina a contagem dos números.
#Repare que, para uma tuple receber um valor vindo de uma variável,
#e necessário colocar () nome da variável mais virgula.

if 9 in valores:

        print(f'O valor 9 apareceu {valores.count(9)} vezes')

if 3 in valores:
        
        print(f'O número 3 aparece na {valores.index(3)+1} posição ')

else:

        print('O valor 3 não foi digitado ')

print('O numeros pares são: ',end=' ')

for numeros in valores:

    if numeros % 2 == 0:
          
          print(numeros,end= ' ' )



















