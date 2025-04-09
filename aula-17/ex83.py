lista = []
exp = input('Digite uma expressão: ')
lista.append(exp)
contagem_parenteses = 0
while lista.count('(') > 0 and lista.count(')') > 0:
    contagem_parenteses = len('()')
    contagem_parenteses += 1
if contagem_parenteses % 2 == 0:
    print('Válido')
else:
    print('Inválido')



# exp = input('Digite uma expressão: ')
# contagem_parenteses = 0
# while True:
#     if '(' in exp:
#         contagem_parenteses += 1
#     if ')' in exp:
#         contagem_parenteses -= 1
#     if contagem_parenteses % 2 == 0:
#         print('Válido')
#         break
#     else:
#         print('Inválido')
#         break