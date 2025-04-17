exp = str(input('Digite sua expressão: ')).split()
lista = []
lista.append(exp)
cont = 0 

for c in lista:
    if c == '(':
        cont += 1
    elif c == ')':
        cont -= 1
        
if cont %2 == 0:
    print('É uma expressão válida!')
    
else:
    print('É uma expressão inválida!!')


# exp = str(input('Digite sua expressão: ')).split()
# cont = 0 

# for c in exp:
#     if c == '(':
#         cont += 1
#     elif c == ')':
#         cont -= 1
        
# if cont %2 == 0:
#     print('É uma expressão válida!')
    
# else:
#     print('É uma expressão inválida!!')