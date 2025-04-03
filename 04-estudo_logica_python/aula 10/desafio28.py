from random import choice
print('Tente adivinhar qualquer numero de 0 a 5')
numeros=[0, 1, 2, 3, 4, 5]
sorteio= choice(numeros)
numeros= int(input(' Digite um numero:'))
if numeros== sorteio:
    print(f'VOCE ACERTOU!! NUMERO:{sorteio}')
else:
    print('numero errado')
    print(f'o numero que estava escondido era {sorteio}') 