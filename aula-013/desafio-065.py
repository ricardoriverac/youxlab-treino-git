cont = 0
media = 0
soma = 0
maior = 0
menor = 99999999
lista = [ ]
quant = 0
while True:
    num = int(input('Digite os valores: '))
    quant += 1
    lista.append(num)
    soma = sum(lista)
    continuar = str(input('Você quer continuar? S/N')).lower()
    while continuar == 's':
        num = int(input('Digite os valores: '))
        quant += 1
        lista.append(num)
        soma = sum(lista)
        continuar = str(input('Você quer continuar? S/N')).lower()
        if num > maior:
            maior = num
        if num <= menor:
            menor = num
        s = soma / quant
    else:
        break

print (f'A média desses números é {s}')
print(f'O maior número é o {maior}')
print(f'O menor número é o {menor}')