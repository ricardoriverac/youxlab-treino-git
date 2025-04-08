numero = contador = acumulador = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar] '))
    if numero != 999:
        contador += 1
acumulador += numero
print('Você digitou {} números e a soma entre eles é {}.'.format(contador, acumulador))