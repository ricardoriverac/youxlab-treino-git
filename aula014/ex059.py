escolha =0
numero1=int(input('Me diga um valor: '))
numero2=int(input('Me giga o segundo: '))

while escolha != 5:

    print(' ')

    escolha=int(input('''Me diga oque deseja fazer com esses números: 
                      
      [1] Some os valores
      [2] Multiplique
      [3] Divida 
      [4] Digitar novos valores
      [5] Sair 
        : '''))

    print('<=>'*20)
    
    if escolha == 1:
        s= numero1 + numero2
        print('Para soma nos temos {} '.format(s))

    elif escolha ==2:
        print('Multiplicando os valores no temos: {} '.format(numero1 * numero2))

    elif escolha ==3:
        print('Na divisão temos: {}'.format(numero1/numero2))

    elif escolha ==4:
        numero1=int(input('Me diga os novos valores de sua escolha: '))
        numero2=int(input('Me diga o segundo novo valor: '))

    else:
        print('FIM do programa,obrigado. ')

    
    
    
    

