from random import randint

quantidade = int(input('Digite quantos sorteios serão: '))

print('<>' * 9)
print('JOGO DA MEGA SENA')
print('<>' * 9)

for jogo in range(quantidade):
    lista = []

    while len(lista) < 6:
        numero = randint(1, 60)

        if numero not in lista:
            lista.append(numero)
    
    lista.sort() 
    print(f'Jogo {jogo}: {lista}')
