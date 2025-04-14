#NÚMERO PRIMO
numero=int(input('Digite um número:'))
total=0
for contador in range(1, numero+1):
    if numero % contador==0:
        total+=1
if total==2:
    print(f'O número {numero} é primo, foi dividido {total} vezes')
else:
    print(f'Número {numero} NÃO é primo, foi dividido {total} vezes')

