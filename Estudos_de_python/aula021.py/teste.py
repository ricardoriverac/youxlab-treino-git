#help(print) or print(input.__doc__)

# def contador(i,f,p):
#     """
#     i -- número inicial
#     f -- número final
#     p -- em quanto em quanto
#     """

#     c = 0
#     while c <= f:
#         print(f'{c}',end = '')
#         c += p

#     print('\nFIM ')

# contador(3,20,2)

# help(contador)



# def soma(a=1,b=4,c=3):
#     """
#     a-- primeiro valor
#     b-- segundo valor
#     c-- terceiro valor
#     s-- soma dos tres valores
#     """

#     s = a + b + c
#     print(f'A soma vale {s}')


# soma(3,2)

# help(soma)


# def valores(l=1,n=2,s =3):
#      valorGrande = 10
#      soma = l + n + s          #Escopo local
#      print(soma)
#      print('{pequeno}')

# l = 4
# n = 5
# s = 6    #Escopo Global

# print('{valorGrande}')    #Não acontece nada,pois essa variavel so tem valor no Escopo Local
# soma = l + n + s
# print(soma)
# valores(l,n,s)
# pequeno = 2



# def funcao():
#     n1 = 4
#     print(f'N1 dentro vale {n1}')


# n1 = 2
# funcao()
# print(f'N1 fora vale {n1}')


# def teste(b):
#     global a
#     a = 8
#     b += 4
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c} ')

# a = 5
# teste(a) 
# print(f'A fora vale {a}')



# def somar(a=0,b=0,c=0):
#     soma = a + b + c
#     return soma

# resposta1=somar(3,2,1)
# resposta2=somar(2,7)
# resposta3=somar(4)

# print(f'Para soma 1 temos ={resposta1}  ,soma2 ={resposta2} , soma3 ={resposta3}')


