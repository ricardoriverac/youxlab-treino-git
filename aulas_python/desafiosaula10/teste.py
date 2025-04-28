tempo = int(input('Quantos anos seu carro tem? '))
if tempo<=3:
    print('Seu carro está novo')
else:
    print('Carro velho')
print('--FIM--')

tempo = int(input('Quantos anos seu carro tem? '))
print('Carro novo'if tempo<=3 else 'Carro velho')

nome = input('Qual seu nome? ')
if nome == 'Gustavo':
    print('Que nome lindo você tem! ')
else:
    print('Seu nome é tão normal! ')
print('Bom dia {}! '.format(nome))

nota = float(input('Primeira nota: '))
nota2 = float (input('Segunda nota: '))
n = (nota + nota2)/2
print('A média da sua nota foi {}'.format(n))
if n<=6:
    print('Sua média não foi boa, melhore!')
else:
    print('Sua média foi boa, parabéns!')
print('PARABÉNS!' if n >=6 else 'ESTUDE MAIS!')
