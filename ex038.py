#consertar
numero1= int(input('Digite um número: '))
numero2= int(input('Digite um novo número: '))
if numero1 > numero2:
    print('O número {} é o primeiro maior número'.format(numero1))
if numero2 > numero1:
    print('O número {} é o primeiro maior número'.format(numero2))
if numero1 < numero2:
    print('O número {} é o segundo maior número').format(numero1)
if numero2 < numero1:
    print('O número {} é o segundo maior número'.format(numero2))
else:
    numero1 == numero2
    print('Não existe valor maior, os dois são iguais')