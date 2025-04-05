numero = quant = soma = 0
while True:
    numero = int(input('Digite um número (999 pra parar): '))
    if numero == 999:
        break
    quant += 1
    soma += numero
print(f'Você digitou {quant} números e a soma deles é {soma}')