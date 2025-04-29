exerc = str(input("Digite uma expressão"))
lista = []
for simbo in exerc:
    if simbo == "(":
        lista.append("(")
    elif simbo == ")":
        if len(lista)> 0:
            lista.pop()
        else:
            lista.append(")")
            break
if len(lista)==0:
    print("Sua expressao esta valida:")
else:
    print("Expressão invalida")
    