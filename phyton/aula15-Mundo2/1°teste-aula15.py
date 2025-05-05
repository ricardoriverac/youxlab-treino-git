#COMANDO BREAK
numero=soma=0
while True:#enquanto infinito 
    numero=int(input('Digite um n°: '))
    if numero==999: #se n° igual 999
         break      #Acaba
    soma+=numero #soma os  n° antes de 999
print(f'A soma dos valores é {soma}')

    