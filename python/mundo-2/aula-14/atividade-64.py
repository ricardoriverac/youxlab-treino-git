print('== Soma de Vários Números ==')
print('(Digite 999 para parar)\n')

soma = 0
contador = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    contador += 1

print(f'\nVocê digitou {contador} números e a soma entre eles foi {soma}.')
