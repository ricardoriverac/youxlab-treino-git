def vparenteses(expressao):
    lista= []

    for caractere in expressao:
        if caractere == '(':
            lista.append(caractere)
        elif caractere == ')':
            if not lista:
                return False
            lista.pop()

    return not lista
expressao = input("Digite uma expressão: ")

if vparenteses(expressao):
    print("Os parênteses estão corretamentos!")
else:
    print("Os parênteses estão incorretos")