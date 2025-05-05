lista = [4, 6, 2, 7]     

def maior(lista):
    maiorNum = lista[0]
    for numero in lista:
        if numero > maiorNum:
            maiorNum = numero
    return maiorNum

maiorNumero = maior(lista)
print(f'O maior número da lista é o {maiorNumero}')


# def maior(lista):
#     maiorNum = max(lista)
#     return maiorNum

# maiorNumero = maior(lista)
# print(f'O maior número da lista é {maiorNumero}')