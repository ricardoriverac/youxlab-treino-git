from datetime import datetime

ano=int(input('Que ano que você nasceu? '))
anoatual=datetime.now().year
anoA=anoatual-ano
anoB= 18 - anoA

if anoA<18:
    print('Você nao precisa se alistar ainda. Faltam {} anos para você se alistar'.format(anoB))
elif anoA==18:
    print('Está no ano para você se alistar')
else:
    print('Já passou da hora de você se alistar')
