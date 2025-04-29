import time
print('\033[1;34m-=-=-=-=-= P.A. v2.0 =-=-=-=-=-\033[m')
time.sleep(1)

print('\n\033[1;34m-=-=-=-=-= 10 TERMOS DE P.A. =-=-=-=-=-\033[m')
termo1  = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
contador = 0
quantos = 10

while contador < quantos:
    print(termo1, end= ' ')
    termo1 += raz
    contador += 1

    if contador == quantos:
    
        mais = str(input('\nVocê quer ver mais termos? S/N '))
        if mais in 'sS' :
            quantos = int(input('Mais quantos termos? '))
            contador = 0 
     
        elif mais in 'Nn':
            print('Programa encerrado :( ')
