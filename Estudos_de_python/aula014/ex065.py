
soma=0
escolha=''
c=0

while escolha !='N':

    valor=int(input('Escolha um número: '))

    c += 1

    if c ==1:
        menor = valor
        maior = valor


    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

    soma += valor
    media= valor/c
    

    escolha=str(input('Quer continuar?[S/N]: ')).upper()
 

print('O maior número e {} e menor e {} '.format(maior,menor))
print('A media e {} a soma e {} '.format(media,soma))

        














