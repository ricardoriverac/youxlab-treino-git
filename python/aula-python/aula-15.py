numero= soma= 0
while True:
    numero= int(input('Digite um número: '))
    if numero==18:
        break
    soma += numero
print(f'A soma vale {soma}')
