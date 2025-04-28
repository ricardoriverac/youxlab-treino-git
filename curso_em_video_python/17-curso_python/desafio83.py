print('\033[1mDIGITE UMA EXPRESSÃO QUE TENHA \033[1;35mPARÊTENSES\033[m')
lista = ' '
expressao = input('\033[1mDigite aqui: \033[m')
parentese = expressao.count('(')
parentese2 = expressao.count(')')
if parentese == parentese2:
    print('Sua expressão está certa.')
else:
    print('Sua expressão está errada.')