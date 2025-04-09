isRodando = True
lista = []
quant = 0
while isRodando:
    num = int(input('Digite um número'))
    if num == 999:
        break
    quant += 1
    lista.append(num)
    soma = sum(lista)
    
print(f'A soma entre esses números é {soma}')
print(f'Foram digitados {quant}')
