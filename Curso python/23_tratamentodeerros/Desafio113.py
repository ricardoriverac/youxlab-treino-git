parar = False
while parar == False:  
    try:
        num = int(input('Digite um número: '))      
    except ValueError:
        print('\033[31mERRO!. DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m') 
    else:
        print(f'Número digitado foi {num}')
        parar = True