from random import choice
print('Vamos jogar jokenpô ?')
lista=['pedra', 'papel', 'tesoura']
computador=choice(lista) 
print(' escolha uma opçao')
print('[1] pedra')
print('[2] papel')
print('[3] tesoura ')

opcao=input('Qual a sua escolha ? ')
print(opcao)
print(computador)
if computador ==1 and opcao ==2 or computador==2 and opcao==3 or computador==3 and opcao==1:
    print('VOCÊ GANHOU!!')
elif computador ==1 and opcao ==1 or computador==2 and opcao==2 or computador==3 and opcao==3:
     print(' VOCÊ EMPATOUU ')
else :
     print(' VOCÊ   PERDEUUU')