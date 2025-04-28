primeiraNota = float(input('Primeira nota: '))
segundaNota = float(input('Segunda nota: '))
media = (primeiraNota + segundaNota)/2
if media<5.0:
    print('Você foi {}REPROVADO!{}'.format('\033[31m', '\033[m'))
elif media<=5.0 or media<=6.9:
    print('Você está de {}RECUPERAÇÃO!{}'.format('\033[33m', '\033[m'))
elif media>=7.0:
    print('PARABÉNS! Você está {}APROVADO!{}'.format('\033[36m', '\033[m'))
