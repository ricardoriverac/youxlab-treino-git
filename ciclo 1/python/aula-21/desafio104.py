def leiaInt(frase):
    num=input(frase)
    while num.isnumeric()==False:
        print('ERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.')
        num=input(frase)
    print(f'Você acabou de digitar o número {num}')
num=leiaInt('Digite um número: ')