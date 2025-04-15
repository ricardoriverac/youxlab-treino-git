text = int(input('digite um número: '))
choice = int(input(''' escolha uma forma de converção: 
    [1] BINÁRIO
    [2] OCTAL
    [3] HEXADECIMAL
    Escolha: '''))
if choice == 1:
    print(text, '->', bin(text)[2:])
elif choice == 2:
    print(text, '->', oct(text)[2:])
else:
    print(text, '->', hex(text)[2:])