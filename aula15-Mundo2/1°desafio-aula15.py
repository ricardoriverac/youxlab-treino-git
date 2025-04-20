numero=soma=0
contador=0
while True:
    numero=int(input('Digite um número:'))
    if numero==999:
        break
    contador+=1
    soma+=numero
print(f'Foram {contador} numeros digitados e a soma desses valores é de {soma}')