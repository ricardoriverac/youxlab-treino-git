
#MÉDIA, MAIOR E MENOR VALORES 
resposta='S'
soma= quantidade= media=maior= menor=0
while resposta in 'Ss':
    numero=int(input('Digite um n°: '))
    soma+=numero
    quantidade+=1
    resposta=str(input('Quer continuar? [s/n]: ')).upper().strip()[0] #maiúscula,removeu os espaços e sera considerado a 1° letra
    if quantidade==1:
        maior=menor=numero
    else:
        if numero>maior:
            maior=numero
        if numero<menor:
            menor=menor
media=soma/quantidade
print('VocÊ digitou {} números e a média deles é de {:.2f}'.format(quantidade,media))
print(f'O maior número foi {maior} e o menor foi {menor}')