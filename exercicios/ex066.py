numero= 0
contador= 0
soma= 0
while True:
    numero= int(input('Digite um valor: '))
    if numero==999:
        break
    soma+=numero
    contador+=1
print(f'Você digitou {contador} \n A soma desses números é ={soma: .2f}')