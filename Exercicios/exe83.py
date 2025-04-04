#Crie um programa onde o usuario digite uma expressão qualquer que use parentese
#Seu aplicativo devera analisar se a expressão passada está com os parentese abertos
#e fechados na ordem correta.

expressao = input("Digite a expressão: ")
caixa = []
temParentese = False

for caractere in expressao:
    if caractere == "(":
        caixa.append("(")
        temParentese = True
    elif caractere == ")":
        temParentese = True
        if len(caixa) > 0:
            caixa.pop()
        else:
            print("Expressão inválida! Fechamento sem abertura.")
            break
else:
    if len(caixa) == 0 and temParentese:
        print("Expressão válida!")
    else:
        print("Expressão inválida! Abertura sem fechamento ou sem parênteses.")
