n1 = int(1)
n1 = int(11)
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da P.A.: '))
while n < n1:
    an = a1 + (n - 1 )* r
    print (an, end= ', ')
    n += 1  
    if n == n1:
        print('Pause')
        n1 += int(input("Quantos termos a mais deseja visualizar? "))
        continue
    elif (n1 == 0):
        break
print(f'Programa encerrado, com {n} termos mostrados')