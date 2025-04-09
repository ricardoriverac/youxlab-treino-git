print('\033[1;34m-=-=-=-=-= Maior e Menor valores =-=-=-=-=-\033[m')
resp = 'S'
soma = quant = media = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    
    if quant == 1:
        maior = menor = num
        
    else:
        if num > maior:
            maior = num
            
        if num < menor:
            menor = num
        
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print(F'Você digitou {quant} números e a média foi {media}!')
print(F'O maior valor foi {maior} e o menor {menor}')