numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite outro número: '))
#maior numero
if numero1 > numero2 and numero1 > numero3:
    print(f'O maior número é {numero1}')
if numero2 > numero1 and numero2 > numero3:
    print(f'O maior número é {numero2}')
if numero3 > numero1 and numero3 > numero2:
    print(f'O maior número é {numero3}')
#menor numero
if numero1 < numero2 and numero1 < numero3:
    print(f'O menor número é {numero1}')
if numero2 < numero1 and numero2 < numero3:
    print(f'O menor número é {numero2}')
if numero3 < numero1 and numero3 < numero2:
    print(f'O menor número é {numero3}')
else:
    print('')