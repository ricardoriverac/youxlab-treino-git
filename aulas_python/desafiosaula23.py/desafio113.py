def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro!\033[m ')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar os dados! ')
            return 0
        else:
            return n

def leiafloat (msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número real!\033[m ')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar os dados! ')
            return 0
        else:
            return n
     
numeroUm = leiaInt('Digite um número inteiro: ')
numeroDois = leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {numeroUm} e o número real digitado foi {numeroDois}')
