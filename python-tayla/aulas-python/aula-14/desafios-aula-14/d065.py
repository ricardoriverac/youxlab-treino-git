resposta = 'S'
media = soma = quantidade = 0
maior = 0
menor = 0
while resposta in 'Ss':
    numero = int(input('Digite um número: '))

    #calculando media
    soma += numero
    quantidade += 1 

    #calculando maior e menor
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor: 
            menor = numero 

    resposta = input('Quer continuar? [S/N] ').upper()
media = soma / quantidade
print('-=' * 12)
print(f'Você digitou {quantidade} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')