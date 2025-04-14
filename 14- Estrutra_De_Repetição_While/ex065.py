r = 'S'

contador = 0

soma = 0

maior = menor = numero = 0

while r == 'S':

    numero =int(input('Digite um valor: '))

    r = str(input('Quer continuar? [S/N]: ')).upper()
    contador += 1   
    soma += numero
    media = soma / contador

    if contador == 1:
        maior = menor = numero
        
    else:
        if numero > maior:
            maior = numero
            
        if numero < menor:
            numero = menor


print(F'Você digitou {contador} números e a média foi {media}!')
print(F'O maior valor foi {maior} e o menor {menor}')

 










