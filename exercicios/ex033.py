numero1= int(input('Digite um número: '))
numero2= int(input('Digite outro número: '))
numero3= int(input('Digite mais um: '))
if numero1 > numero2 and numero3:
    print('{} é o maior número'.format(numero1))
if numero2 > numero1 and numero3:
    print('{} é o maior número'.format(numero2))
if numero3 > numero1 and numero2:
    print('{} é o maior número'.format(numero3))
if numero1 < numero2 and numero3:
    print('{} é o menor número'.format(numero1))
if numero2 < numero1 and numero3:
    print('{} é o menor número'.format(numero2))
if numero3 < numero1 and numero2:
    print('{} é o menor número'.format(numero3))
     

