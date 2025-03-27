num = int(input('Me diga um número qualquer: '))
if num % 2 == 0 :
    print('Esse número é \033[0;31mPAR\033[m')
else:
    print('Esse número é \033[0;31mIMPAR\033[m')    