exp = str(input('Digite sua expressão: '))
cont = 0 

for c in exp:
    if c[:] == '(':
        cont += 1
    if c[:] == ')':
        cont += 1
        
if cont %2 == 0:
    print('É uma expressão válida!')
    
else:
    print('É uma expressão inválida!!')