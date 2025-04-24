n = total = cont = 0
while n != 999:
    n = int(input('Digite um número inteiro ou 999 para parar: '))
    if n != 999:
        total += n
        cont += 1
print('Foram digitados {} números e a soma entre eles foi {}'.format(cont, total))