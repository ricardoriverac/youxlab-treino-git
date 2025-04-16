condicao = 0
soma = 0
while True:
    numero = int(input('Digite um número: ( Digite 999 para parar): '))
    if numero == 999:
        break
    condicao+= 1
    soma += numero
print(f'Foram digitados ao todo {condicao} números e a soma entre eles é {soma}')
