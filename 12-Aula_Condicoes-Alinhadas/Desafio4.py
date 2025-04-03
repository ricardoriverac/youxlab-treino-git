ano=int(input('em qual ano nasceu ? '))
data = 2025 - ano
data2 = 18 - data
if data == 18:
    print('Você deve se alisatar esse ano !!')
elif data > 18:
    print('Ja passou a hora de se alistar!! ')
elif data < 18:
    print('Não e a hora ainda, falta {}'.format(data2))    


