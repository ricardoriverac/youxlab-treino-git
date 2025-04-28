sexo = True
resposta = ''
while resposta != 'M' and resposta != 'F':
    resposta = str(input('Qual seu sexo?[F/M]: ').upper())
    if resposta != 'M' and resposta != 'F':
      print('RESPOSTA INVALIDA! Tente novamente: ')
    else:
        print('Valor correto! ')
    
    
    