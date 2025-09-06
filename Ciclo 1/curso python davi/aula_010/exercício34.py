s=float(input('qual o seu salário? '))
if s>1250:
    a=10/100
    sa=s+(s*a)
    print('seu novo salário com 10% será {}'.format(sa))
else: 
    a=15/100
    sa=s+(s*a)
    print('seu novo salário com 15% será {}'.format(sa))