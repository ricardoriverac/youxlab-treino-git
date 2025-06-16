# numero = str(input("Digite uma expressão: "))
# paren = [] #lista que vai receber os parenteses.
# for p in numero: #para cada parenteses em numero
#     if p == '(': #se parenteses for parenteses abrindo: ela vai para lista
#         paren.append('(')
#     elif p == ')': #senão se tiver parenteses fechando
#         if len(paren) > 0: #o comprimento do parenteses for acima de 0 remove 
#             paren.pop()
#         else:
#             paren.append(')')
#             break
# if len(paren) == 0:
#     print('A expressão esta correta!')
# else:
#     print('Sua expressão esta errada!')

expressao = str(input("Digite uma expressão numérica: "))
listaParenteses = []
parenFechado = []
for paren in expressao:
    if paren == '(':
        listaParenteses.append(paren)
    elif paren == ')':
        parenFechado.append(paren)
if len(listaParenteses) == len(parenFechado):
    print('Sua expressão esta correta!')
else:
    print('Sua expressão esta errada!')

