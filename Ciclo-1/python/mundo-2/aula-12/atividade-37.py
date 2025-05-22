numero = int(input('Digite um número: '))
converta = int(input('Você deseja converter esse número para:\n'
      '1) binário\n'
      '2) octal\n'
      '3) hexadecimal\n'))
if converta == 1:
    print(bin(numero))
elif converta == 2:
    print(oct(numero))
elif converta == 3:
    print(hex(numero))
else:
    print('Escolha uma opção válida.')