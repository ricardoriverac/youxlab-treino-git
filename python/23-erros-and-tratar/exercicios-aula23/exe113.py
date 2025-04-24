def leiaint(msg=''):
    while True:
        try:
            leia = int(input(msg))
        except (ValueError , AttributeError , TypeError):
            print('\033[31mERRO: Digite o número inteiro válido! TENTE NOVAMENTE...\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário decidiu optar o codigo\033[m')
            return 0
        else: 
            return int(leia)
            
        
def leiaFloat(msg=''):
    while True:
        try:
            leia = float(input(msg))
        except (ValueError , AttributeError, TypeError):
            print('\033[31mERRO: Digite o número real válido! TENTE NOVAMENTE...\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário decidiu optar o codigo\033[m')
            return 0
        else:
            return float(leia)

#programa principal

inteiro = leiaint('Digite um número inteiro: ')
real = leiaFloat('Digite o número real: ')
print(f'O número que você digitou inteiro é {inteiro} e o real é {real}')
