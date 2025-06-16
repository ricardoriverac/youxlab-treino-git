nome = input('Digite o nome de uma pessoa:')
sexo = input('Fale o sexo dessa pessoa F/M:').lower().strip()[0]
while sexo != 'm' and sexo != 'f':
    print('Tente de novo:')
    sexo = input('Fale o sexo dessa pessoa F/M:').lower()
else:
    print('ok')



