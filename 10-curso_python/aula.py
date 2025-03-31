carro = int(input('Quantos anos tem o seu carro? '))
if carro <=3 : 
    print ('Seu carro ainda está novo.')
else :
    print('Seu carro já está velho.')
print('  FIM  ') 

carro = int(input('Quantos anos tem o seu carro? '))
print('carro novo'if carro <=3 else 'carro velho')

nome = input('Qual o seu nome? ')
if nome == 'Ana' :
    print ('Seu nome é lindo!')
else :
    print('Nome feio.')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('Sua média é: {:.1f}.'.format(m))
if m >=6.0 :
    print('Sua média é boa.')
else :
    print('Melhore.')