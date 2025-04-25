lista = ['zero', 'um', 'dois', 'três', 'Quatro', 'Cinco',
         'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'onze',
         'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 
         'Dezessete', 'Dezoito', 'Dezenove', 'vinte']

num = int(input('Digite um número entre 0 e 20: '))
while num > 20:
    print("Não aceitamos esse valor. Tente de novo!")
    num = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {lista[num]}')




# lanche = ['hamburguer', 'pizza', 'suco', 'pudim']
# for lanche in lanche:
#     print(lanche[3]) #mostra o terceiro termo de cada item na lista
# import random
# suco = 'bebida'
# lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
# for cont in range(0, len(lanche)):
#     print(f'Vou comer {lanche[cont]}')
# print('Comi pra caramba!')

# def saudacao():
#     print(f'Olá, seja bem vindo! {nome}')
# nome = str(input('Qual é o seu nome?'))
# if nome == 'kev':
#     saudacao()


