def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\33[0;31mUsuário preferiu não digitar esse número.\33[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = str(input(msg))
            n = float(n.replace(',', '.'))
        except(ValueError, TypeError):
            print('\33[0;31mERRO! Digite um número real válido\33[m')
            continue
       
        else:
            return n


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')