numero = int(input('Escolha um número qualquer: '))
print ("""Escolha uma das bases para conversão:
       [ 1 ] - converter para Binário     
       [ 2 ] - converter para Octal       
       [ 3 ] - converter para Hexadecimal""")
escolha = int(input('Selecione uma opção: '))
if escolha == 1:
    print (f'{numero} convertido para binário é {bin(numero)[2:]} ')
elif escolha == 2:
    print (f'{numero} convertido para binário é {oct(numero)[2:]} ')
elif escolha == 3:
    print (f'{numero} convertido para binário é {hex(numero)[2:]} ')