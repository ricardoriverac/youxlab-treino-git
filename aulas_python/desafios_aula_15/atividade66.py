print('\033[1;34m-=-=-=-=-= 999 =-=-=-=-=-\033[m')
soma = 0 
while True:
    resposta = int(input('Digite um número [999 para parar]: '))
    soma = soma + resposta 
    
    if resposta == 999:
        soma = soma -999
        print(f'A soma dos números que você digitou antes de 999 é: {soma}!')
        break

    

    