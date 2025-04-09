#while True:
primeiroTermo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
limite = int(input('Digite o limite:'))
cont = 1
termo = primeiroTermo
while cont <= limite:
    print(f'{termo} ', end= '')
    termo += razao
    cont += 1

#n = 11
#an = primeiroTermo + (n - 1) * razao
#for i in range (primeiroTermo, an, razao):
    #print(i)
    
