numero = int(input('Escreva um valor:'))

resultado = 1

count = 1

while count <=numero:

    if count == 1:
        print(f'{count} = ', end="")

    else:
        print(f'{count} x ', end="")
        
    resultado *= count 
    count += 1 


print(resultado, end=   '')


