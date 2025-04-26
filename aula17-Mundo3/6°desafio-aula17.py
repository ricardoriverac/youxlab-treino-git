#VALIDANDO EXPRESSOẼS
expressao=str(input('Digite sua expressão: '))
parenteses=[]
for simbolo in expressao:
    if simbolo=='(':
        parenteses.append('(')
    elif simbolo==')':
        if len(parenteses)>0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses)==0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão NÃO é válida!')