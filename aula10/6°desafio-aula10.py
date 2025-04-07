numero1=int(input('Digite um número:'))
numero2=int(input('Digite um número:'))
numero3=int(input('Digite um número:'))
if numero1<numero2 and numero1<numero3:#SE n°1 for MENOR o que n°2 E MENOR que o n°3 O NUMERO 1 É O MENOR 
    menor=numero1
if numero2<numero1 and numero2<numero3:
    menor=numero2
if numero3<numero1 and numero3<numero2:
    menor=numero3
print(f'o MENOR número é : {menor}')
if numero1>numero2 and numero1>numero3:#SE n°1 for MENOR o que n°2 E MENOR que o n°3 O NUMERO 1 É O MENOR 
    maior=numero1
if numero2>numero1 and numero2>numero3:
    maior=numero2
if numero3>numero1 and numero3>numero2:
    maior=numero3
print(f'o MAIOR número é : {maior}')