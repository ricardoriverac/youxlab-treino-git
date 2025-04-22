def leiaint(msg):
    numero = input(msg)
    while not numero.isnumeric() or ' ' in numero:
        numero = input('\033[0;31mERRO! Por favor, digite apenas números: \033[m')
    return int(numero)
        

text = leiaint('Digite um número: ')
print(f'Você digitou o número {text}.')