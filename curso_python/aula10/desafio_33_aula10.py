numero1 = (input('Digite um valor: '))
numero2 = (input('Digite outro valor: '))
numero3 = (input('Digite mais um valor: '))
if numero1 > numero2 and numero1 > numero3:
    print (f'O maior número é {numero1}')
elif numero2 > numero1 and numero2 > numero3:
    print (f'O maior número é {numero2}')
elif numero3 > numero1 and numero3 > numero2: 
    print (f'O maior número é {numero3}')
else:
    print ('')
if numero1 < numero2 and numero1 < numero3:
    print (f'O menor número é {numero1}')
elif numero2 < numero1 and numero2 < numero3:
    print (f'O menor número é {numero2}')
elif numero3 < numero1 and numero3 < numero2:
    print (f'O menor número é {numero3}')

# numero1 = (input('Digite um valor: '))
# numero2 = (input('Digite outro valor: '))
# numero3 = (input('Digite mais um valor: '))
# menor = numero1
# if numero2 < numero1 and numero2 < numero3:
#     menor = numero2
# if numero3 < numero1 and numero3 < numero2:
#     menor = numero3

# maior = numero1
# if numero2 > numero1 and numero2 > numero3:
#     maior = numero2
# if numero3 > numero1 and numero3 > numero2:
#     maior = numero3
#     print (f'O menor número é o {menor}')
#     print (f'O maior número é o {maior}')