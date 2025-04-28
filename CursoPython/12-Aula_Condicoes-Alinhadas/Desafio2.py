num1=int(input('Numero de sua escolha '))
print("""Essas são as conversões:
[ 1 ]- Binario
[ 2 ]- Octal
[ 3 ]- Hexadeciaml""")
op = int(input('Escolha sua opção:  '))
if op == 1:
    print('o seu numero {} fica em Binario {}'.format(num1, bin(num1)))
elif op ==2:
    print('O seu numero {} em Octal fica {}'.format(num1, oct(num1)))
elif op ==3:
    print('O seu numero {} em Hexadecimal e {}'.format(num1, hex(num1)))

