# def linha():
#     print('<>'*15)

# linha()
# print('Olá Mundo!! ')
# linha()

# def tilulo(txt):

#     print('<>'*20)
#     print(txt)
#     print('<>'*20)

# tilulo('Nicolas gosta de bolo ')
# tilulo('Maria está brincando de bola ')

# def soma(numero1,numero2):
#     soma = numero1 + numero2
#     print(f'A soma de {numero1} + {numero2} = {soma}')


# #Comando principal
# soma(numero2=4,numero1=5)
# soma(2,6)
# soma(7,3)

# def contador(*numeros):
#     for valor in numeros:
#         print(f'{valor} ',end =' ')
#     print( )

# contador(2,4,7,4,3,6,2,4,8,9,4,2)
# contador(3,4,2,5,7,4,5,2)
# contador(5,6,8,4,6,)


def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1


valores = [2,4,63,4,6,3,6]
dobra(valores)
print(valores) 



