jogador = contador = soma = 0
condicaoDeParada = 999
while jogador != 999:
    numero = int(input('Digite um número: '))
    contador+=1
    soma+=numero
    if numero==999:
        print('ACABOU')
        break
print('Você digitou {} NÚMEROS e a SOMA deles é {} '.format(contador-1, soma-999))
