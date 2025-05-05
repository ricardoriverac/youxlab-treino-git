from random import choice
print('Vamos jogar jokempo? ')
lista=('pedra','papel', 'tesoura')

computador = choice(lista)  
print('Escolha uma opção')
print(' [1] pedra ')
print('[2] papel ')
print('[3] tesoura')

opcao=input('Qual a sua escolha? ')
print(opcao)
print(computador)
if computador == 1 and opcao == 2 or computador ==2 and opcao == 3 or computador ==3 and opcao==1:
    print('VOCE GANHOUUUUU!!!!!!')

elif computador == 1 and opcao == 1 or computador ==2 and opcao == 2 or computador ==3 and opcao==3:
    print('VOCE EMPATOU')
else:
    print('VOCE PERDEU')