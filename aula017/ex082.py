valores =[]
par=[]
impar=[]

while True:

    valores.append(int(input('Me diga um numero: ')))
    resposta=str(input('Deseja continuar [S/N]: ').upper())

    if resposta == 'N':
        break

    #valor =(input('Digite um valor: '))
    #valores.append(valor) 


for numero in valores:
        
        if numero % 2 == 0:
            par.append(numero)

        else:
             impar.append(numero)


print(valores)
print( )
print(f'{par} .Esses são os valores pares ')
print( )
print(f'{impar}. Esses são os impares')


    










