numero = int(input(' Digite os termos:'))
termo_um = 0
termo_dois = 1
print('{} -> {}'.format(termo_um, termo_dois), end='')
contador = 3
while contador<= numero: 
    termo_tres = termo_um + termo_dois
    print(" -> {}" .format(termo_tres), end='')
    termo_um = termo_dois
    termo_dois = termo_tres
    contador  += 1
print("-> Fim!")