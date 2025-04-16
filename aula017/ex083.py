conta =str(input('Digite uma expressão: '))
parenteses =[]
parenteses2 =[]

for simbulo in conta:
    
    if simbulo == '(':
        parenteses.append(simbulo)

    elif simbulo == ')':
        parenteses2.append(simbulo) 

if len(parenteses) == len(parenteses2) and len(parenteses2) == len(parenteses):
    print('A expressão está OK ')

else:
    print('Não está correto ')



        
        
