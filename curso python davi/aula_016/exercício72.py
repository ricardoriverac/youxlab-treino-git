cont = ('zero ', 'um', 'dois',
'três', 'quatro', 'cinco',
'seis', 'sete', 'oito', 
'nove', 'dez', 'onze',
'doze', 'treze' ,''
'quatorze', 'quinze',
'dezesseis', 'dzsete', 
'dzoito', 'dznove', 'vinte')
while True:
    núm = int(input('diga um número de 0 a 20: '))
    if 0 <= núm <= 20:
        break
    print('tente novamente. ', end='')
    print(f'vc digitou o número{cont[núm]}')