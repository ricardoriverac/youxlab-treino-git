def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido\033[m')
            continue

        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não digitar os dados!\033[m')
            return 0
        else:
            return numero

def leiaFloat(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número real válido\033[m')
            continue

        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não digitar os dados!\033[m')
            return 0
        else:
            return numero
    
inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi \033[1;33m{inteiro}\033[m e o real foi \033[1;33m{real}\033[m')