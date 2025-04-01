numero1 = int(input('Escolha um número inteiro: '))
numero2 = int(input('Escolha mais um número: '))
if numero1 > numero2:
    print('O primeiro valor é \033[1;36mmaior\033[m')
elif numero2 > numero1:
    print('O segundo valor é \033[1;36mmaior\033[m')
else:
    print('Não existe valor maior, os dois são \033[1;32miguais\033[m')