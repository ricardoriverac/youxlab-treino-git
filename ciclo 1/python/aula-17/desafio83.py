expressao = input("Digite a expressão: ")
lista = []
for i in expressao:
    if i == '(' or i == ')':
        lista.append(i)
check = 0
for j in lista:
    if j == '(':
        check += 1
    elif j == ')':
        check -= 1
    if check < 0:
        break
if check == 0:
    print('Expressão CORRETA!')
else:
    print('Expressão ERRADA!')
