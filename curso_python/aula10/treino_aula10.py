nome = (input('Qual é o seu nome? '))
if nome == 'Vinícius':
   print ('Que nome lindo você tem! ')
else:
   print ('Seu nome é tão normal! ') 
print (f'Bom dia, {nome}! ')

# usual
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1 + nota2) /2
print (f'A sua média foi de {m:.1f}')
if m >= 6.0:
    print ('Sua média foi boa! Parabéns! ')
else:
   print ('Sua média não foi muito boa...Tente novamente! ')

# alternativa
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1 + nota2) /2
print (f'A sua média foi de {m:.1f}')
print ('Sua média foi boa! Parabéns!' if m >=6 else 'Sua média não foi muito boa...Tente novamente! ')