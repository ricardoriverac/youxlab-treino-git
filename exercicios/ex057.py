m= 'M'
f= 'F'
sexo= ''
while sexo != m and sexo != f:
    sexo= str(input('Informe seu sexo: ')).upper() .capitalize()
    if sexo == m and sexo == f:
       
       print('Seu sexo é masculino!')
    else:
        sexo != f  
        if sexo == f:
            print('Seu sexo é feminino!')
