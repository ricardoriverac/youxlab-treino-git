m= 'M'
f= 'F'
sexo= ''
while sexo != m and sexo != f:
    sexo= str(input('Informe seu sexo: ')).upper() .capitalize()
    if sexo != m and f:
        print('INVÁLIDO!')

    if sexo == m and sexo == f:
       
       print('Seu sexo é masculino!')

    if sexo == f:
            print('Seu sexo é feminino!')
