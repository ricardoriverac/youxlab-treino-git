expressao = input("Digite uma expressão com parênteses: ")

pilha = []

for caractere in expressao:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break  

if len(pilha) == 0:
    print("A expressão está com os parênteses CORRETOS.")
else:
    print("A expressão está com os parênteses INCORRETOS.")
