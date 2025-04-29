numero= 0

priNumero = int(input('Me diga um valor: '))

segNumero = int(input('Me diga o segundo: '))

while numero != 5:

    print(' ')

    numero=int(input('''Me diga oque deseja fazer com esses números: 
                      
      [1] Some os valores
      [2] Multiplique
      [3] Divida 
      [4] Digitar novos valores
      [5] Sair 
        : '''))

    print('<=>'*20)
    
    if numero == 1:
        s= segNumero + priNumero
        print('Para soma nos temos {} '.format(s))

    elif numero ==2:
        print('Multiplicando os valores no temos: {} '.format(priNumero * segNumero))

    elif numero ==3:
        print('Na divisão temos: {}'.format(priNumero/segNumero))

    elif numero ==4:
        priNumero=int(input('Me diga os novos valores de sua escolha: '))
        segNumero=int(input('Me diga o segundo novo valor: '))

    else:
        print('FIM do programa,obrigado. ')
