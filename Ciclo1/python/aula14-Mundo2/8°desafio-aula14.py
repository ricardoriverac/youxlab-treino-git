#TRATANDO VALORES
numeros=0
contador=0
soma=0
numeros=int(input('Digite o número que deseje somar (999 para parar): '))
while numeros!=999:
    soma+=numeros
    contador+=1
    numeros=int(input('Digite o número que deseje somar (999 para parar): '))
print(f'Você digitou {contador} números e a soma desses valores é {soma}')