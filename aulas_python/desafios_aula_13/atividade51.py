import time

print('\033[1;34m-=-=-=-=-= Bem vindo(a)! =-=-=-=-=-\033[m')
time.sleep(1)


print('\n\033[1;34m-=-=-=-=-= 10 TERMOS DE P.A. =-=-=-=-=-\033[m')
a1  = int(input('Primeiro termo: '))
pos = int(input('Termo final: '))
raz = int(input('Razão: '))

for c in range(a1, pos, raz):
    print(F'✦{c}✦', end= ' ' )
    
print('\033[1;34m-=-=-=-=-= FIM! =-=-=-=-=-\033[m')