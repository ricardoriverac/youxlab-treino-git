numero1= int(input('Digite o primeiro numero:'))
numero2= int(input(' Digite o segundo numero:'))
numero3=int(input('Digite o terceiro numero:'))
numero4=int(input(' Digite o quarto numero:'))
tupla=(numero1, numero2,numero3, numero4)

print(tupla)
count=0
count9=0
countPosicao=0
valoresOares=[]

for t in tupla:
    if t==9:
        count9+=1
    if t == 3:
        countPosicao = count
    count+=1

    if t % 2 == 0:
        valoresOares.append(t)
print(f'apareceu o numero nove {count9} vezes')
print(f' o numeros pares sao: {valoresOares}')
print(f'o numero 3 encontra na posiçao {countPosicao}')
