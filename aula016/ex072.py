
valores = ('zero','Um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez', \
'onze','doze','treze','catorze','quinze','decesseis','decessete','dezoito','dezenove' 'vinte ')

while True:
     numero=int(input('Me diga um valor entre 0 e 20: '))
     
     if numero <= 20 or numero == 0:
         break
     
     print('Tente novamente...')

print(f'Você digitou o numero {valores[numero]}')

     
     
















