numero = 1
totalNumeros = 0 
soma = 0

while numero != 999:
    numero = int(input('Digite um número inteiro: '))
    if numero != 999:
        totalNumeros += 1
        soma += numero

print(f'Voce digitou \033[1;36m{totalNumeros}\033[m números e a soma deles é \033[1;36m{soma}\033[m')