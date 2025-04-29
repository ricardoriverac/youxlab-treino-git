from random import randint
print('Vamos jogar par ou ímpar?: ')
escolha= int(input('''Escolha uma das suas opções: 
      [1] ÍMPAR
      [2] PAR
      DIGITE AQUI: '''))
computador= randint(0, 10)
numero= 0
soma= 0
par= impar= 0
perder= True
count= 0
while perder==True:
    numero=int(input('Agora... um número entre 0 e 10: '))
    soma= computador + numero
    if soma % 2 ==0 and escolha== 2:
        print('Você ganhou! Jogue novamente...')
        print(f'O computador escolheu: {computador} e você escolheu {numero}')
        count+=1
    if soma % 2 != 0 and escolha== 1:
        print('Você ganhou! Jogue novamente...')
        print(f'O computador escolheu: {computador} e você escolheu {numero}')
        count+=1
    else:
            print('Computador ganhou, você perdeu. Patinho!')
            print(f'Computador escolheu {computador}, você escolheu {numero}.')
            break
print(f'Você ganhou {count} vezes!')



    