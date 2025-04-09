print('\033[1;34m-=-=-=-=-= 999 =-=-=-=-=-\033[m')

teste = 999
teste = False

resposta = int(input('Digite um número [999 para parar]: '))

if resposta != 999:
    while True:
        resposta = int(input('Digite um número [999 para parar]: '))
        
        soma = resposta + resposta - 999
        
        if resposta == 999:
            print(f'A soma dos números que você digitou antes de 999 é: {soma}')
            break

    

    