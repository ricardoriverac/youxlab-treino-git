contador= 0
soma= 0
numero= 0
while numero != 999:
    numero= int(input('Digite um número inteiro: '))
    soma += numero
    contador += 1
    if numero == 999:
        soma -= numero
        contador -= 1
print(f'Você digitou {contador} números.')
print(f'A soma entre esses números é ={soma}')
