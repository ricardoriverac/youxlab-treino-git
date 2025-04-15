numero = soma = 0
valores = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    else:
        soma += numero
        valores += 1
print(f'Foram digitados {valores} valores. A soma é {soma}.')