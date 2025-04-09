idade= int(input('Informe sua idade: '))
if idade > 18:
    print('Já passou do tempo de alistamento!')
elif idade == 18:
    print('É a hora de se alistar!')
elif idade < 18:
    print('Ainda não é hora de se alistar!')